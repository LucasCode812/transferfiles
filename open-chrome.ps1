# Set the URL of the PHP script that retrieves the variables
$url = "http://localhost/script.php"

# Invoke the PHP script and retrieve the variables
$data = Invoke-RestMethod -Uri $url -Method POST

# Retrieve the variables from the data object
$naam = $data.naam
$achternaam = $data.achternaam
$functie = $data.functie

# Build the URL for the new Chrome tab
$tabUrl = "https://www.google.com/search?q=$naam+$achternaam+$functie"

# Open the URL in a new Chrome tab
$chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
Start-Process $chromePath $tabUrl
