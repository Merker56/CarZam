package main

import (
	"bytes"
	"fmt"
	rs "github.com/nfnt/resize"
	"image"
	"image/draw"
	"image/jpeg"
	"io/ioutil"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

var newSize = 224
var stretch = false
var inputDir = "."
var outputDir = "./resized"

var makeModelClass = map[string]int{}

func main() {
	parseArgs()
	inputFileNames := getInputFiles()
	for _, fileName := range inputFileNames {
		resize(fileName)
	}
}

func parseArgs() {
	fmt.Println("Usage: cropper inputDir outputDir newSize stretch")
	fmt.Println("Example: cropper ./raw/F150 ./resized/F150 224 false")
	if len(os.Args) > 1 {
		inputDir = os.Args[1]
		fileInfo, err := os.Stat(inputDir)
		if err != nil {
			fmt.Printf("Error opening input directory %s: %v\n", inputDir, err)
			os.Exit(1)
		}
		if !fileInfo.IsDir() {
			fmt.Printf("Input directory %s is not a directory\n", inputDir)
			os.Exit(1)
		}
	}
	if len(os.Args) > 2 {
		outputDir = os.Args[2]
		fileInfo, err := os.Stat(outputDir)
		if err == nil {
			if !fileInfo.IsDir() {
				fmt.Printf("Output directory %s is not a directory\n", outputDir)
				os.Exit(1)
			}
		} else {
			os.MkdirAll(outputDir, 0777)
		}
	}
	if len(os.Args) > 3 {
		num := os.Args[3]
		var err error
		newSize, err = strconv.Atoi(num)
		if err != nil {
			fmt.Printf("Error parsing new size %s: %v\n", num, err)
			os.Exit(1)
		}
	}
	if len(os.Args) > 4 {
		var err error
		stretch, err = strconv.ParseBool(os.Args[4])
		if err != nil {
			fmt.Printf("Error parsing strecth %s: %v\n", os.Args[4], err)
			os.Exit(1)
		}
	}
	fmt.Printf("Input directory: %s\n", inputDir)
	fmt.Printf("Output directory: %s\n", outputDir)
	fmt.Printf("New Size: %d\n", newSize)
	fmt.Printf("Stretch: %v\n", stretch)
}

func getInputFiles() []string {
	result := []string {}

	filepath.Walk(inputDir, func(path string, fileStat os.FileInfo, err error) error {
		if !fileStat.IsDir() && strings.HasSuffix(path, ".jpg") {
			result = append(result, path[len(inputDir):])
		}
		return nil
	})

	return result
}

func resize(path string) {
	img := readImage(path)
	if img == nil {
		return
	}
	var rect image.Rectangle
	var newDimension int
	if !stretch {
		img, newDimension, rect = pad(img)
		rect = resizeRect(rect, newDimension)
	} else {
		rect = image.Rectangle{
			Min: image.Point{0, 0},
			Max: image.Point{newSize, newSize},
		}
	}
	resized := rs.Resize(uint(newSize), uint(newSize), img, rs.MitchellNetravali)
	writeImage(path, resized)
	writeAnnotation(path, rect)
}

func writeAnnotation(path string, rect image.Rectangle) {
	splits := strings.Split(path, "-")
	makeModel := splits[1] + splits[2]
	classNum, ok := 0, false
	if classNum, ok =  makeModelClass[makeModel]; !ok {
		classNum = len(makeModelClass)
		makeModelClass[makeModel] = classNum
	}

	annotationPath := strings.Replace(path, ".jpg", ".txt", -1)
	outPath := filepath.Join(outputDir, annotationPath)
	outFile, err := os.Create(outPath)
	if err != nil {
		fmt.Printf("Error creating %s: %v\n", outPath, err)
		return
	}
	width := rect.Max.X - rect.Min.X
	height := rect.Max.Y - rect.Min.Y
	outFile.WriteString(fmt.Sprintf("%d %d %d %d %d\n", classNum, rect.Min.X, rect.Min.Y, width, height))
	outFile.Close()
}

func readImage(path string) image.Image {
	fullPath := filepath.Join(inputDir, path)
	raw := getRaw(fullPath)
	image, err := jpeg.Decode(bytes.NewReader(raw))
	if err != nil {
		fmt.Printf("Error with %s: %v\n", path, err)
		return nil
	}
	return image
}

func pad(img image.Image) (image.Image, int, image.Rectangle) {
	prevWidth := img.Bounds().Max.X - img.Bounds().Min.X
	prevHeight := img.Bounds().Max.Y - img.Bounds().Min.Y
	newDimension := prevWidth
	if prevHeight > newDimension {
		newDimension = prevHeight
	}
	newImage := image.NewRGBA(image.Rectangle{
		Min: image.Point{0, 0},
		Max: image.Point{newDimension, newDimension},
	})
	destinationPoint := image.Point{0, 0}
	if prevHeight > prevWidth {
		destinationPoint.X = (newDimension - prevWidth) / 2
	} else {
		destinationPoint.Y = (newDimension - prevHeight) / 2
	}
	destRect := image.Rectangle{
		Min: image.Point{destinationPoint.X, destinationPoint.Y},
		Max: image.Point{destinationPoint.X +  prevWidth, destinationPoint.Y + prevHeight},
	}
	draw.Draw(newImage, destRect, img, image.Point{0, 0}, draw.Src)
	return newImage, newDimension, destRect
}

func writeImage(path string, resized image.Image) {
	outPath := filepath.Join(outputDir, path)
	outDir := filepath.Dir(outPath)
	err := os.MkdirAll(outDir, 0777)
	if err != nil {
		fmt.Printf("Error creating directory %s: %v\n", outDir, err)
		return
	}
	outFile, err := os.Create(outPath)
	if err != nil {
		fmt.Printf("Error creating %s: %v\n", outPath, err)
		return
	}
	jpeg.Encode(outFile, resized, nil)
	outFile.Close()
}

func getRaw(fileName string) []byte {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Printf("Cannot read file %s", fileName)
	}
	return data
}

func resizeRect(before image.Rectangle, newDimension int) image.Rectangle {
	ratio := float32(newSize) / float32(newDimension)
	result := image.Rectangle{
		Min: image.Point{int(float32(before.Min.X) * ratio), int(float32(before.Min.Y) * ratio)},
		Max: image.Point{int(float32(before.Max.X) * ratio), int(float32(before.Max.Y) * ratio)},
	}
	return result
}