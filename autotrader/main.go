package main

import (
	"fmt"
	"github.com/tidwall/gjson"
	"io/ioutil"
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"
	"path/filepath"
	"time"
)

const minYear = "2010"
const maxYear = "2020"
const maxImagesPerModel = 1000
var imageDir = "/Users/adminwk/w210/autotrader/images"

//const searchUrlTemplate = "https://www.autotrader.com/rest/searchresults/base?zip=63101&makeCodeList={{makeCode}}&modelCodeList={{modelCode}}&startYear={{minYear}}&endYear={{maxYear}}&searchRadius=1000&sellerTypes=p&maxPrice=200000&sortBy=derivedpriceASC&numRecords=20000&firstRecord={{firstRecord}}"
const searchUrlTemplate = "https://www.autotrader.com/rest/searchresults/base?zip=63101&makeCodeList={{makeCode}}&modelCodeList={{modelCode}}&startYear={{minYear}}&endYear={{maxYear}}&searchRadius=1000&maxPrice=200000&sortBy=derivedpriceASC&numRecords=20000&firstRecord={{firstRecord}}"
const detailPageUrlTemplate = "https://autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId={{id}}"

func main() {
	makeModels["TOYOTA"] = nil
	makeModels["HONDA"] = nil
	makeModels["FORD"] = nil
	makeModels["CHEV"] = nil
	for makeCode, models := range makeModels {
		for _, modelCode := range models {
			pageNumber := 0
			for {
				pageNumber++
				searchResponse := primarySearch(makeCode, modelCode, pageNumber)
				listings := getListings(string(searchResponse))
				fmt.Printf("Found %d listings for %s %s (page %d) ", len(listings), makeCode, modelCode, pageNumber)
				for _, listing := range listings {
					setImageUrls(listing)
					writeImages(listing)
					fmt.Printf(".")
				}
				fmt.Printf("\n")
				if len(listings) == 0 {
					break  //we're done with this model - no more results
				}
				if 25 * pageNumber > maxImagesPerModel {
					break //we got the max we need
				}
			}
		}
	}
}

func setImageUrls(listing *listing) {
	if listing.primaryImg != "" {
		listing.imageUrls = []string{listing.primaryImg}
		return
	}
	detailPageUrl := strings.Replace(detailPageUrlTemplate, "{{id}}", listing.id, -1)
	detailPageBody := mustGetHttp(detailPageUrl)
	re, err := regexp.Compile(`"//images.autotrader.com/[^"]+` + listing.id + `[^"]+.jpg"`)
	if err != nil {
		fmt.Printf("%v", err)
	}
	imageUrls := re.FindAllString(string(detailPageBody), -1)
	//listing.imageUrls = dedup(imageUrls)
	if len(imageUrls) > 0 {
		listing.imageUrls = []string{imageUrls[0]}
	}
}

func primarySearch(make string, model string, pageNumber int) []byte {
	searchUrl := strings.Replace(searchUrlTemplate, "{{makeCode}}", make, -1)
	searchUrl = strings.Replace(searchUrl, "{{modelCode}}", model, -1)
	searchUrl = strings.Replace(searchUrl, "{{minYear}}", minYear, -1)
	searchUrl = strings.Replace(searchUrl, "{{maxYear}}", maxYear, -1)
	searchUrl = strings.Replace(searchUrl, "{{firstRecord}}", strconv.Itoa((pageNumber - 1) * 25), -1)
	responseBody := mustGetHttp(searchUrl)
	return responseBody
}

func getListings(searchResponse string) []*listing {
	result := make([]*listing, 0)
	idsJson := gjson.Get(searchResponse, "listings.#.id")
	makesJson := gjson.Get(searchResponse, "listings.#.make")
	makes := makesJson.Array()
	modelsJson := gjson.Get(searchResponse, "listings.#.model")
	models := modelsJson.Array()
	yearsJson := gjson.Get(searchResponse, "listings.#.year")
	years := yearsJson.Array()
	for i, id := range idsJson.Array() {
		imagesJson := gjson.Get(searchResponse, "listings." + strconv.Itoa(i) + ".images.sources.0.src")
		primaryImage := imagesJson.Str
		listing := &listing{
			id:    fmt.Sprintf("%d", id.Int()),
			make:  makes[i].String(),
			model: models[i].String(),
			year:  years[i].String(),
			primaryImg: primaryImage,
		}
		result = append(result, listing)
	}
	return result
}

func writeImages(listing *listing) {
	subDir := filepath.Join(imageDir, listing.make, listing.model)
	os.MkdirAll(subDir, 0700)
	for imgNum, url := range listing.imageUrls {
		fileName := listing.year + "-" + listing.make + "-" + listing.model + "-" + listing.id + "-img" + strconv.Itoa(imgNum) + ".jpg"
		fullFileName := filepath.Join(subDir, fileName)
		_, err := os.Stat(fullFileName)
		if os.IsNotExist(err) {
			urlStripped := strings.Replace(url, `"`, ``, -1)
			imgUrl := "https:" + urlStripped
			imageData := mustGetHttp(imgUrl)
			ioutil.WriteFile(fullFileName, imageData, 0600)
		}
	}
}


func mustGetHttp(url string) []byte {
	response, err := http.Get(url)
	if err != nil {
		fmt.Printf("Http error: %v", err)
		os.Exit(1)
	}
	result, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Printf("Http read error: %v", err)
	}
	response.Body.Close()
	time.Sleep(time.Duration(5) * time.Second)
	return result
}

func dedup(vals []string) []string {
	m := make(map[string]int)
	for _, val := range vals {
		m[val] = 0
	}
	result := make([]string, 0)
	for k, _ := range m {
		result = append(result, k)
	}
	return result
}