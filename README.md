# AgriMarket

### **Data Source:** 
[Agmarknet](https://agmarknet.gov.in/Default.aspx) portal is a GOI (Govt of India) portal on agricultural marketing. The Portal provides both static and dynamic information relating to agricultural marketing in India . 
- The static information is about infrastructure- related (Storage, warehousing, Cold Storage, grading and packing facilities), Market – related (market fee/ charges, weighment, handling, market functionaries, development programmes, market laws, composition of market Committees, income and expenditure, etc) and Promotion-related information (Standards, Grades, Labelling, Sanitary and Phyto-Sanitary requirements, Pledge Financing, Marketing Credit and new opportunities available, etc.). 
- The dynamic part comprise Price-related information comprising maximum, minimum and modal prices of varieties, total arrivals and dispatches with destination. The portal provides easy access to commodity-wise, variety-wise daily prices and arrivals information of more than 2000 varieties and about 300 commodities from the wholesale markets spread all over the country.


## **Script:**
### **1. What?**
- The Script is aimed to scrape the Historical data from the website of all the different commodities (~350) for 4000+ markets present on the website. However it can also be used to extract daily prices with little modification.

### **2. How?**
- The Script uses Selenium and BeautifulSoup to extract the data. Selenium is used to interact with In-Page elements and BeautifulSoup to pull out data from the HTML document.
- Since the webpage allows only 50 rows to be loaded at a time, I used Selenium to interact with "Next" button on the page to allow next 50 rows to be populated and extracted from its HTML.
- BeautifulSoup is one of the most popular libraries out there to extract data from HTML and XML files.

### **3. Challenges, Drawbacks and Concerns!**
- Being a govt. site, it requires a bit of patience to let it load the data in the background. 
- The Dataset could be very large depending on the time period. I have used sleep statements to go along with the loading process of the website. To put things into perspective, just Potato for Year 2020 had more than 164k rows. And since each page only shows 50 rows, this might take a long time to run.
- Theoretically it can be scaled by horizontal scaling, distributed computing and multithreading to fetch data for multiple or all commodities together.

### **4. Why?**
- The purpose of this project was to brush up web-scraping concepts and specifically Selenium and BeautifulSoup.

### **5. How to use this project?**
- You can learn about Selenium and BeautifulSoup concepts through the code. I have added comments and documentation for every method.
- You can also use this to download a reasonable amount of data through this and use it for your Time-Series Forecasting or Analytics & Visualization projects.

### **6. Things to Note:**
- This being a govt site, I believe that the servers on the backend are not powerful or smart enough to handle these many requests. 
> I would advise you to play with the script only to learn and not to wreck govt servers as thousands of people rely on this data everyday

Happy Learning! :metal: 


