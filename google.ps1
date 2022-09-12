#!/usr/bin/env powershell


function googleSearch {
	start https://google.com/?q=$args
}

Set-Alias google googleSearch
