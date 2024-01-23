# AirBnB MongoDB Analysis

## Data Set Details

The data set is of AirBnB listings from Chicago, Illinois, United States, and the data set file is retrieved from [here](http://insideairbnb.com/get-the-data/), which is in CSV format. And some of the raw data looks like following (some fields have been clipped to avoid line-wrapping):

| id | listing_url | scrape_id | last_scraped | source | name | description | neighborhood_overview | picture_url | host_id | host_url | host_name | host_since | host_location | host_about | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url | host_picture_url | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications | host_has_profile_pic | host_identity_verified | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type | room_type | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities | price | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|2384 | https://www.airbnb.com/rooms/2384 | 20230319041143 | 2023/3/19 | city scrape | Hyde Park - Walk to UChicago | You | The | https://a0.muscache.com/pictures/acf6b3c0-47f2-463e-902b-d13dfd66668f.jpg | 2613 | https://www.airbnb.com/users/show/2613 | Rebecca | 2008/8/29 | Chicago, IL | "My | within an hour | 100% | 97% | t | https://a0.muscache.com/im/pictures/user/8bb4745c-c262-42e6-bb8d-4e8f4b638f8e.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/8bb4745c-c262-42e6-bb8d-4e8f4b638f8e.jpg?aki_policy=profile_x_medium | Hyde Park | 1 | 1 | ['email', 'phone'] | t | t | Chicago, Illinois, United States | Hyde Park | | 41.7879 | -87.5878 | Private room in condo | Private room | 1 | | 1 shared bath | 1 | 1 | ["Dedicated | $90.00 | 3 | 89 | 3 | 3 | 1125 | 1125 | 3 | 1125 | | t | 19 | 45 | 72 | 347 | 2023/3/19 | 212 | 20 | 1 | 2015/1/9 | 2023/3/4 | 4.99 | 4.98 | 4.99 | 4.99 | 4.99 | 4.96 | 4.93 | R17000015609 | f | 1 | 0 | 1 | 0 | 2.13 |
| 1772920 | https://www.airbnb.com/rooms/1772920 | 20230319041143 | 2023/3/19 | city scrape | 3 Bedroom Across from Wrigley Field AllStar Suite | Welcome | Besides | https://a0.muscache.com/pictures/28490752/b4cc2a0e_original.jpg | 9297431 | https://www.airbnb.com/users/show/9297431 | Inn At Wrigleyville | 2013/10/8 | Chicago, IL | The | within an hour | 100% | 100% | t | https://a0.muscache.com/im/pictures/user/dcf7dc2a-3134-4ac1-b05c-6562cfe4e5c3.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/dcf7dc2a-3134-4ac1-b05c-6562cfe4e5c3.jpg?aki_policy=profile_x_medium | Lakeview | 6 | 6 | ['email', 'phone', 'work_email'] | t | f | Chicago, Illinois, United States | Lake View | | 41.94842 | -87.65307 | Entire rental unit | Entire home/apt | 7 | | 2 baths | 3 | 5 | ["Oven" | $379.00 | 1 | 365 | 2 | 3 | 365 | 1125 | 2.4 | 447.5	| | t | 24 | 48 | 72 | 206 | 2023/3/19 | 13 | 3 | 0 | 2013/12/1 | 2022/8/21 | 4.67 | 4.67 | 4.75 | 4.42 | 4.75 | 4.92 | 4.58 | 2446868 | t | 6 | 6 | 0 | 0 | 0.11 |
| 1773021 | https://www.airbnb.com/rooms/1773021 | 20230319041143 | 2023/3/19 | city scrape | 4 Bedroom Across from Wrigley Field Stadium Suite | Welcome | Besides | https://a0.muscache.com/pictures/28491077/6edb454a_original.jpg | 9297431 | https://www.airbnb.com/users/show/9297431 | Inn At Wrigleyville | 2013/10/8 | Chicago, IL | The | within an hour | 100% | 100% | t | https://a0.muscache.com/im/pictures/user/dcf7dc2a-3134-4ac1-b05c-6562cfe4e5c3.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/dcf7dc2a-3134-4ac1-b05c-6562cfe4e5c3.jpg?aki_policy=profile_x_medium | Lakeview | 6 | 6 | ['email', 'phone', 'work_email'] | t | f | Chicago, Illinois, United States | Lake View | | 41.94774 | -87.65421 | Entire rental unit | Entire home/apt | 9 | | 2 baths | 4 | 5 | ["Laundromat | $479.00 | 1 | 365 | 2 | 3 | 365 | 1125 | 2.4 | 447.5 | | t | 24 | 41 | 59 | 215 | 2023/3/19 | 26 | 10 | 1 | 2021/4/18 | 2023/3/12 | 4.92 | 4.92 | 4.92 | 4.96 | 4.88 | 5 | 4.85 | 2446868| t | 6 | 6 | 0 | 0 | 1.11 |
| 1773025 | https://www.airbnb.com/rooms/1773025 | 20230319041143 | 2023/3/19 | city scrape | 4 Bedroom Across from Wrigley Field Legend Suite | Welcome | Besides | https://a0.muscache.com/pictures/28489088/cb9d55cf_original.jpg | 9297431 | https://www.airbnb.com/users/show/9297431 | Inn At Wrigleyville | 2013/10/8 | Chicago, IL | The | within an hour | 100% | 100% | t | https://a0.muscache.com/im/pictures/user/dcf7dc2a-3134-4ac1-b05c-6562cfe4e5c3.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/dcf7dc2a-3134-4ac1-b05c-6562cfe4e5c3.jpg?aki_policy=profile_x_medium | Lakeview | 6 | 6 | ['email', 'phone', 'work_email'] | t | f | Chicago, Illinois, United States | Lake View | | 41.9475 | -87.6542 | Entire rental unit | Entire home/apt | 9 | | 2 baths | 4 | 5 | ["Oven" | $479.00 | 1 | 365 | 2 | 3 | 365 | 1125 | 2.4 | 447.5 | | t | 27 | 52 | 69 | 223 | 2023/3/19 | 21 | 7 | 0 | 2021/4/18 | 2022/9/12 | 4.86 | 5 | 4.81 | 4.95 | 4.9 | 5 | 4.76 | 2446867 | t | 6 | 6 | 0 | 0 | 0.9 |
| 1810118 | https://www.airbnb.com/rooms/1810118 | 2.02303E+13 | 2023/3/19 | city scrape | LARGE Private 1BR/Full Bath near U of Chicago | LARGE | Wake | https://a0.muscache.com/pictures/miso/Hosting-1810118/original/8eeb4f7d-081d-4c2a-9931-0b5ca270b8d9.jpeg | 9483312 | https://www.airbnb.com/users/show/9483312 | Ryan | 2013/10/17 | Chicago, IL | Hope | within an hour | 100% | 100% | t | https://a0.muscache.com/im/pictures/user/0f326f05-1077-4dd2-87ff-1b5c700be4bd.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/0f326f05-1077-4dd2-87ff-1b5c700be4bd.jpg?aki_policy=profile_x_medium | Woodlawn | 2 | 2 | ['email', 'phone'] | t | f | Chicago, Illinois, United States | Woodlawn | | 41.77738 | -87.60041 | Private room in home | Private room | 3 | | 1 private bath | 1 | 1 | ["Self check-in" | $79.00 | 4 | 90 | 4 | 4 | 90 | 90 | 4 | 90 | | t | 0 | 23 | 40 | 105 | 2023/3/19 | 355 | 12 | 0 | 2014/2/20 | 2022/11/20 | 4.89 | 4.93 | 4.93 | 4.96 | 4.96 | 4.48 | 4.88 | R17000015592 | f | 2 | 1 | 1 | 0 | 3.21 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

There are no problems that were present in the data, and thus I did not perform any data scrubbing with the data.

## Analysis
1. show exactly two documents from the listings collection in any order

- Code
```
let orderBy = { "id": 1 }

db.listings.find().sort(orderBy).limit(2)
```

<details>

<summary> All Two Results</summary>
[
  {
    _id: ObjectId("6434617024ed498386a4d768"),
    id: 2384,
    listing_url: 'https://www.airbnb.com/rooms/2384',
    scrape_id: Long("20230319041143"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Hyde Park - Walk to UChicago',
    description: 'You are invited to be the sole Airbnb guest in my vintage, 2nd floor co-op guest room. This Hyde Park location is convenient for visiting The University of Chicago or attending a convention or conference at McCormick Place. The listing is 1 block from the eastern border of UChicago,  a 7 minute walk to Chicago Theological Seminary, and a 16 minutes door-to-door ride to McCormick Place via the Metra Electric train.<br /><br /><b>The space</b><br />The private guest room has a queen size bed, bedside tables w/lamps, a chest of drawers, a desk and chair, and a smart TV.  The large closet contains plenty of hangers, an iron and ironing board, a garment steamer, and extra bedding. There is room in the closet to store your luggage. A window A/C is installed in the guest bedroom during summer months. <br /><br />All bedding (including mattress pad and duvet cover or quilt) is freshly laundered for each guest. During extended stays, weekly housekeeping is provided to the guest room at no addit',
    neighborhood_overview: "The apartment is less than one block from beautiful Jackson Park which houses the Museum of Science and Industry and the Garden of the Phoenix, built for the 1893 World's Columbian Exposition. Theaters, restaurants, grocery stores, book stores, and lakefront bicycle/running paths are within walking distance. This Hyde Park location is served by both the city and  UChicago police departments.<br /><br />My building is located almost next door to the Metra Electric train station, providing you with quick and inexpensive transportation to downtown Chicago.  You need to be aware that the tradeoff for this convenience is the noise from occasional passing freight trains.",
    picture_url: 'https://a0.muscache.com/pictures/acf6b3c0-47f2-463e-902b-d13dfd66668f.jpg',
    host_id: 2613,
    host_url: 'https://www.airbnb.com/users/show/2613',
    host_name: 'Rebecca',
    host_since: '2008-08-29',
    host_location: 'Chicago, IL',
    host_about: "My 2 bdrm apartment is a 2nd floor walk-up in a quiet, vintage co-op building, overlooking a pleasant courtyard.  I allow only one guest so you don't have to worry about other strangers in the apartment. (I occupy the 2nd bedroom).  A single traveler will probably feel safe and be comfortable here. If you are visiting the University of Chicago - or visiting your UChicago student who hasn't enough room to host you - my location should allow you to walk to your destination. My Airbnb listing is also convenient to the Chicago Theological Seminary. \n" +
      '\n' +
      'Please let me know the purpose of your trip to Chicago so I can help you determine if my apartment (or Hyde Park location) is right for your visit.  I may even be able to suggest a more appropriate location. In any event, I will answer your inquiries quickly and honestly. ',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '97%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/8bb4745c-c262-42e6-bb8d-4e8f4b638f8e.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/8bb4745c-c262-42e6-bb8d-4e8f4b638f8e.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Hyde Park',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'Hyde Park',
    neighbourhood_group_cleansed: '',
    latitude: 41.7879,
    longitude: -87.5878,
    property_type: 'Private room in condo',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Dedicated workspace", "Host greets you", "Baking sheet", "Free dryer \\u2013 In building", "Blender", "First aid kit", "Books and reading material", "Bed linens", "Free washer \\u2013 In building", "Carbon monoxide alarm", "Conditioner", "Body soap", "Toaster oven oven", "Essentials", "Hangers", "Shampoo", "Free street parking", "Fast wifi \\u2013 176 Mbps", "Piano", "Iron", "Coffee maker", "Fire extinguisher", "Long term stays allowed", "Shower gel", "Coffee", "Hair dryer", "Hot water", "Clothing storage: dresser and closet", "Smoke alarm", "Kitchen", "Cleaning available during stay", "Toaster", "Heating", "Cleaning products", "Extra pillows and blankets", "Portable fans", "Gas stove", "Wine glasses", "Paid parking garage off premises", "40\\" HDTV with Amazon Prime Video, Chromecast, Hulu, Netflix", "Dishes and silverware", "Hot water kettle", "Dining table", "Bathtub", "Courtyard view", "Refrigerator", "Microwave", "Cooking basics"]',
    price: '$90.00',
    minimum_nights: 3,
    maximum_nights: 89,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 3,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 19,
    availability_60: 45,
    availability_90: 72,
    availability_365: 347,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 212,
    number_of_reviews_ltm: 20,
    number_of_reviews_l30d: 1,
    first_review: '2015-01-09',
    last_review: '2023-03-04',
    review_scores_rating: 4.99,
    review_scores_accuracy: 4.98,
    review_scores_cleanliness: 4.99,
    review_scores_checkin: 4.99,
    review_scores_communication: 4.99,
    review_scores_location: 4.96,
    review_scores_value: 4.93,
    license: 'R17000015609',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.13
  },
  {
    _id: ObjectId("6434617124ed498386a4f5b2"),
    id: 7126,
    listing_url: 'https://www.airbnb.com/rooms/7126',
    scrape_id: Long("20230319041143"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Tiny Studio Apartment 94 Walk Score',
    description: 'A very small studio in a wonderful neighborhood.<br /><br /><b>The space</b><br />This is a very small  studio apartment with a private entrance. <br /><br />The apartment is located on the rear half of our first floor. It has its own entrance. It consists of a kitchen and a very small bedroom with a queen sized bed  and bathroom with a tub and shower.  There is a kitchen with a stove and mini fridge and sink and microwave plus a small table for two. We have a Roku Box for tv watching and excellent cable internet. The Roku has Amazon Prime, Netflix, HBO and a bunch of other channels. We have hi-speed Comcast internet <br />I teach an Airbnb Experience in Soapmaking upstairs in my apartment, so let me know if you want to schedule a class at your convenience while you are here!<br /><br /><b>Guest access</b><br />You will be in your own private, tiny apartment. You will not see me or my family at all unless you run into us outdoors or need assistance. You will be provided with easy self-',
    neighborhood_overview: `Ukrainian Village was just named "Hottest Neighborhood in America" by Trulia. Our address has a walk score of 94 because it has an awesome combination of places to walk to, public transportation options and rental bikes all over the place.   (The bike score is a 96)  <br />We are in a convenient location one block away from multiple bars, restaurants, boutiques, etc. you can walk to the El from the apartment (1/2 mile) and take it straight downtown to the museums or to O'Hare airport in the other direction.   Our neighborhood is called Ukrainian Village and we are a historic district which means most of the buildings are old and the neighborhood has lots of character.  We were granted this status in part because it is an unusual neighborhood with numerous Orthodox churches and cathedrals. It is a nice place to walk around. You can walk to the Ukrainian Institute of Modern Art Museum and the Ukrainian National Museum. You can also get Ukrainian food and pastries.  The neighborhood has c`,
    picture_url: 'https://a0.muscache.com/pictures/51073/16c81c7e_original.jpg',     
    host_id: 17928,
    host_url: 'https://www.airbnb.com/users/show/17928',
    host_name: 'Sarah',
    host_since: '2009-05-19',
    host_location: 'Chicago, IL',
    host_about: 'We live in Chicago. We love to travel and see the world with our two children!',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '95%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/17928/profile_pic/1259106070/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/17928/profile_pic/1259106070/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Ukrainian Village',
    host_listings_count: 2,
    host_total_listings_count: 2,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'West Town',
    neighbourhood_group_cleansed: '',
    latitude: 41.90166,
    longitude: -87.68021,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Laundromat nearby", "Dedicated workspace", "Oven", "Private entrance", "Luggage dropoff allowed", "Books and reading material", "Bed linens", "Dining table", "Single level home", "Carbon monoxide alarm", "Body soap", "Window AC unit", "Essentials", "Hangers", "Free street parking", "Iron", "Coffee maker", "Fire extinguisher", "Mini fridge", "Long term stays allowed", "Stove", "Room-darkening shades", "Freezer", "Hair dryer", "Hot water", "Clothing storage: dresser and closet", "Smoke alarm", "Kitchen", "Toaster", "Central heating", "Extra pillows and blankets", "Wine glasses", "HDTV", "Hot water kettle", "Dishes and silverware", "Wifi", "Bathtub", "Microwave", "Cooking basics"]',
    price: '$85.00',
    minimum_nights: 2,
    maximum_nights: 60,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 21,
    availability_60: 34,
    availability_90: 42,
    availability_365: 279,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 483,
    number_of_reviews_ltm: 48,
    number_of_reviews_l30d: 2,
    first_review: '2009-07-03',
    last_review: '2023-02-26',
    review_scores_rating: 4.7,
    review_scores_accuracy: 4.85,
    review_scores_cleanliness: 4.56,
    review_scores_checkin: 4.9,
    review_scores_communication: 4.87,
    review_scores_location: 4.88,
    review_scores_value: 4.75,
    license: 'R21000075737',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.89
  }
]
</details>


- Insight: Show two places with smallest id

<br/>
2. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function

- Code
```
let orderBy = { "id": 1 }

db.listings.find().sort(orderBy).limit(10).pretty()
```

<details>

<summary>First Three Results</summary>
[
  {
    _id: ObjectId("6434617024ed498386a4d768"),
    id: 2384,
    listing_url: 'https://www.airbnb.com/rooms/2384',
    scrape_id: Long("20230319041143"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Hyde Park - Walk to UChicago',
    description: 'You are invited to be the sole Airbnb guest in my vintage, 2nd floor co-op guest room. This Hyde Park location is convenient for visiting The University of Chicago or attending a convention or conference at McCormick Place. The listing is 1 block from the eastern border of UChicago,  a 7 minute walk to Chicago Theological Seminary, and a 16 minutes door-to-door ride to McCormick Place via the Metra Electric train.<br /><br /><b>The space</b><br />The private guest room has a queen size bed, bedside tables w/lamps, a chest of drawers, a desk and chair, and a smart TV.  The large closet contains plenty of hangers, an iron and ironing board, a garment steamer, and extra bedding. There is room in the closet to store your luggage. A window A/C is installed in the guest bedroom during summer months. <br /><br />All bedding (including mattress pad and duvet cover or quilt) is freshly laundered for each guest. During extended stays, weekly housekeeping is provided to the guest room at no addit',
    neighborhood_overview: "The apartment is less than one block from beautiful Jackson Park which houses the Museum of Science and Industry and the Garden of the Phoenix, built for the 1893 World's Columbian Exposition. Theaters, restaurants, grocery stores, book stores, and lakefront bicycle/running paths are within walking distance. This Hyde Park location is served by both the city and  UChicago police departments.<br /><br />My building is located almost next door to the Metra Electric train station, providing you with quick and inexpensive transportation to downtown Chicago.  You need to be aware that the tradeoff for this convenience is the noise from occasional passing freight trains.",
    picture_url: 'https://a0.muscache.com/pictures/acf6b3c0-47f2-463e-902b-d13dfd66668f.jpg',
    host_id: 2613,
    host_url: 'https://www.airbnb.com/users/show/2613',
    host_name: 'Rebecca',
    host_since: '2008-08-29',
    host_location: 'Chicago, IL',
    host_about: "My 2 bdrm apartment is a 2nd floor walk-up in a quiet, vintage co-op building, overlooking a pleasant courtyard.  I allow only one guest so you don't have to worry about other strangers in the apartment. (I occupy the 2nd bedroom).  A single traveler will probably feel safe and be comfortable here. If you are visiting the University of Chicago - or visiting your UChicago student who hasn't enough room to host you - my location should allow you to walk to your destination. My Airbnb listing is also convenient to the Chicago Theological Seminary. \n" +
      '\n' +
      'Please let me know the purpose of your trip to Chicago so I can help you determine if my apartment (or Hyde Park location) is right for your visit.  I may even be able to suggest a more appropriate location. In any event, I will answer your inquiries quickly and honestly. ',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '97%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/8bb4745c-c262-42e6-bb8d-4e8f4b638f8e.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/8bb4745c-c262-42e6-bb8d-4e8f4b638f8e.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Hyde Park',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'Hyde Park',
    neighbourhood_group_cleansed: '',
    latitude: 41.7879,
    longitude: -87.5878,
    property_type: 'Private room in condo',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Dedicated workspace", "Host greets you", "Baking sheet", "Free dryer \\u2013 In building", "Blender", "First aid kit", "Books and reading material", "Bed linens", "Free washer \\u2013 In building", "Carbon monoxide alarm", "Conditioner", "Body soap", "Toaster oven oven", "Essentials", "Hangers", "Shampoo", "Free street parking", "Fast wifi \\u2013 176 Mbps", "Piano", "Iron", "Coffee maker", "Fire extinguisher", "Long term stays allowed", "Shower gel", "Coffee", "Hair dryer", "Hot water", "Clothing storage: dresser and closet", "Smoke alarm", "Kitchen", "Cleaning available during stay", "Toaster", "Heating", "Cleaning products", "Extra pillows and blankets", "Portable fans", "Gas stove", "Wine glasses", "Paid parking garage off premises", "40\\" HDTV with Amazon Prime Video, Chromecast, Hulu, Netflix", "Dishes and silverware", "Hot water kettle", "Dining table", "Bathtub", "Courtyard view", "Refrigerator", "Microwave", "Cooking basics"]',
    price: '$90.00',
    minimum_nights: 3,
    maximum_nights: 89,
    minimum_minimum_nights: 3,
    maximum_minimum_nights: 3,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 3,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 19,
    availability_60: 45,
    availability_90: 72,
    availability_365: 347,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 212,
    number_of_reviews_ltm: 20,
    number_of_reviews_l30d: 1,
    first_review: '2015-01-09',
    last_review: '2023-03-04',
    review_scores_rating: 4.99,
    review_scores_accuracy: 4.98,
    review_scores_cleanliness: 4.99,
    review_scores_checkin: 4.99,
    review_scores_communication: 4.99,
    review_scores_location: 4.96,
    review_scores_value: 4.93,
    license: 'R17000015609',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.13
  },
  {
    _id: ObjectId("6434617124ed498386a4f5b2"),
    id: 7126,
    listing_url: 'https://www.airbnb.com/rooms/7126',
    scrape_id: Long("20230319041143"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Tiny Studio Apartment 94 Walk Score',
    description: 'A very small studio in a wonderful neighborhood.<br /><br /><b>The space</b><br />This is a very small  studio apartment with a private entrance. <br /><br />The apartment is located on the rear half of our first floor. It has its own entrance. It consists of a kitchen and a very small bedroom with a queen sized bed  and bathroom with a tub and shower.  There is a kitchen with a stove and mini fridge and sink and microwave plus a small table for two. We have a Roku Box for tv watching and excellent cable internet. The Roku has Amazon Prime, Netflix, HBO and a bunch of other channels. We have hi-speed Comcast internet <br />I teach an Airbnb Experience in Soapmaking upstairs in my apartment, so let me know if you want to schedule a class at your convenience while you are here!<br /><br /><b>Guest access</b><br />You will be in your own private, tiny apartment. You will not see me or my family at all unless you run into us outdoors or need assistance. You will be provided with easy self-',
    neighborhood_overview: `Ukrainian Village was just named "Hottest Neighborhood in America" by Trulia. Our address has a walk score of 94 because it has an awesome combination of places to walk to, public transportation options and rental bikes all over the place.   (The bike score is a 96)  <br />We are in a convenient location one block away from multiple bars, restaurants, boutiques, etc. you can walk to the El from the apartment (1/2 mile) and take it straight downtown to the museums or to O'Hare airport in the other direction.   Our neighborhood is called Ukrainian Village and we are a historic district which means most of the buildings are old and the neighborhood has lots of character.  We were granted this status in part because it is an unusual neighborhood with numerous Orthodox churches and cathedrals. It is a nice place to walk around. You can walk to the Ukrainian Institute of Modern Art Museum and the Ukrainian National Museum. You can also get Ukrainian food and pastries.  The neighborhood has c`,
    picture_url: 'https://a0.muscache.com/pictures/51073/16c81c7e_original.jpg',     
    host_id: 17928,
    host_url: 'https://www.airbnb.com/users/show/17928',
    host_name: 'Sarah',
    host_since: '2009-05-19',
    host_location: 'Chicago, IL',
    host_about: 'We live in Chicago. We love to travel and see the world with our two children!',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '95%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/17928/profile_pic/1259106070/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/17928/profile_pic/1259106070/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Ukrainian Village',
    host_listings_count: 2,
    host_total_listings_count: 2,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    neighbourhood_cleansed: 'West Town',
    neighbourhood_group_cleansed: '',
    latitude: 41.90166,
    longitude: -87.68021,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Laundromat nearby", "Dedicated workspace", "Oven", "Private entrance", "Luggage dropoff allowed", "Books and reading material", "Bed linens", "Dining table", "Single level home", "Carbon monoxide alarm", "Body soap", "Window AC unit", "Essentials", "Hangers", "Free street parking", "Iron", "Coffee maker", "Fire extinguisher", "Mini fridge", "Long term stays allowed", "Stove", "Room-darkening shades", "Freezer", "Hair dryer", "Hot water", "Clothing storage: dresser and closet", "Smoke alarm", "Kitchen", "Toaster", "Central heating", "Extra pillows and blankets", "Wine glasses", "HDTV", "Hot water kettle", "Dishes and silverware", "Wifi", "Bathtub", "Microwave", "Cooking basics"]',
    price: '$85.00',
    minimum_nights: 2,
    maximum_nights: 60,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 21,
    availability_60: 34,
    availability_90: 42,
    availability_365: 279,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 483,
    number_of_reviews_ltm: 48,
    number_of_reviews_l30d: 2,
    first_review: '2009-07-03',
    last_review: '2023-02-26',
    review_scores_rating: 4.7,
    review_scores_accuracy: 4.85,
    review_scores_cleanliness: 4.56,
    review_scores_checkin: 4.9,
    review_scores_communication: 4.87,
    review_scores_location: 4.88,
    review_scores_value: 4.75,
    license: 'R21000075737',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.89
  },
  {
    _id: ObjectId("6434617124ed498386a4f5b3"),
    id: 10945,
    listing_url: 'https://www.airbnb.com/rooms/10945',
    scrape_id: Long("20230319041143"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'The Biddle House (#1)',
    description: "Beautiful first floor apartment in Historic Old Town. Tree-lined street,  walking distance to countless wonderful restaurants, shops and the lakefront. <br /><br />Beyond Charming, Two-bedroom unit, with one queen and one double, a full kitchen and bathroom.<br /><br /><b>The space</b><br />This 1st floor apartment has a queen size bed in one bedroom and a double in the other bedroom. The bathroom has a bathtub and shower.<br /><br />The apartment includes high speed internet (wi-fi) cable tv, private phone lines, and a complimentary washer and dryer in the building. <br /><br />Public transportation is terrific from this location; you can take the train (brown line) downtown in just 10 minutes! <br /><br />You'll be a short walk from the Lincoln Park Zoo, Chicago History Museum, world-famous Second City, great restaurants and bars like Twin Anchors (an old Sinatra hangout), Old Town Social, and Marges.<br /><br /> Max occupancy per apartment is 5. Closest major intersection is North A",
    neighborhood_overview: '',
    picture_url: 'https://a0.muscache.com/pictures/58d1a420-a24b-485e-8342-7ddff83b2994.jpg',
    host_id: 33004,
    host_url: 'https://www.airbnb.com/users/show/33004',
    host_name: 'At Home Inn',
    host_since: '2009-08-21',
    host_location: 'Chicago, IL',
    host_about: "Hi, we're Bob and Liz Biddle, long time Chicagoans and your hosts. We started At Home Inn Chicago in 2000 as a reservation service for bed and breakfasts in Chicago, and have since evolved into one of the city's most-respected sources for vacation rentals, corporate housing, and weekend getaways. \n" +
      '\n' +
      'We provide fully furnished vacation rentals and corporate housing throughout the city in or near Old Town and Lincoln Park.\n' +
      '\n' +
      'We are here to answer all of your questions about Chicago, whether you need a restaurant recommendation, public transit tips, or insider tips on how to experience the Chicago that locals know and love. \n' +
      '\n' +
      'We love this city, especially getting ribs at Twin Anchors in Old Town before a show at Second City.  Topo Gigio is a great local Italian Restaurant and The Gemini Bistro is an excellent choice for fine dining. And Velvet Taco, casual with its own unique style on Lincoln is fabulous!\n' +
      '\n' +
      "The free concerts at Pritzker Pavilion in Millenium Park can't be matched by any city in the world. \n" +
      '\n' +
      "We'd love to help you experience all of this with us and so much more!",      
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '98%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/e23d4143-c790-4849-88a2-b7d9ac8bd873.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/e23d4143-c790-4849-88a2-b7d9ac8bd873.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: 'Old Town',
    host_listings_count: 10,
    host_total_listings_count: 82,
    host_verifications: "['email', 'phone', 'work_email']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: '',
    neighbourhood_cleansed: 'Lincoln Park',
    neighbourhood_group_cleansed: '',
    latitude: 41.91196,
    longitude: -87.63981,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: 2,
    beds: 2,
    amenities: '["Pack \\u2019n play/Travel crib - available upon request", "Radiant heating", "Oven", "Free dryer \\u2013 In building", "Private entrance", "Outdoor furniture", "Bed linens", "Free washer \\u2013 In building", "Carbon monoxide alarm", "Beach access", "Essentials", "Hangers", "Shampoo", "Free street parking", "Iron", "Coffee maker", "Fire extinguisher", "Shared patio or balcony", "TV with standard cable", "Hair dryer", "Hot water", "Smoke alarm", "High chair", "Kitchen", "Lake access", "Air conditioning", "Extra pillows and blankets", "Outdoor dining area", "Gas stove", "Dishes and silverware", "Wifi", "Crib", "Bathtub", "Refrigerator", "Microwave", "BBQ grill", "Cooking basics"]',
    price: '$171.00',
    minimum_nights: 4,
    maximum_nights: 1125,
    minimum_minimum_nights: 4,
    maximum_minimum_nights: 4,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 4,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 4,
    availability_60: 23,
    availability_90: 36,
    availability_365: 99,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 60,
    number_of_reviews_ltm: 19,
    number_of_reviews_l30d: 0,
    first_review: '2014-04-28',
    last_review: '2023-01-02',
    review_scores_rating: 4.65,
    review_scores_accuracy: 4.75,
    review_scores_cleanliness: 4.8,
    review_scores_checkin: 4.8,
    review_scores_communication: 4.78,
    review_scores_location: 4.98,
    review_scores_value: 4.65,
    license: 2209984,
    instant_bookable: 't',
    calculated_host_listings_count: 10,
    calculated_host_listings_count_entire_homes: 10,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.55
  }
]
</details>

- Insight: Show ten places with smallest id

<br/>
3. choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts

- Code
```
let fields = { _id: 0, "name": 1, "price": 1, "neighbourhood": 1, "host_name": 1, "host_is_superhost": 1 }
let filter = { host_id: { $in: [2613, 9297431] } }

db.listings.find(filter, fields)
```

<details>

<summary>First Three Results</summary>
[
  {
    name: 'Hyde Park - Walk to UChicago',
    host_name: 'Rebecca',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    price: '$90.00'
  },
  {
    name: '3 Bedroom Across from Wrigley Field AllStar Suite',
    host_name: 'Inn At Wrigleyville',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    price: '$379.00'
  },
  {
    name: '4 Bedroom Across from Wrigley Field Stadium Suite',
    host_name: 'Inn At Wrigleyville',
    host_is_superhost: 't',
    neighbourhood: 'Chicago, Illinois, United States',
    price: '$479.00'
  }
]
</details>

- Insight: Show all listings offered by two specific super hosts

<br/>
4. find all the unique host_name values

- Code
```
db.listings.distinct("host_name")
```

<details>

<summary>First Three Results</summary>
[
  '(Email hidden by Airbnb)',
  '2 Level Up',
  '747 Lofts Concierge'
]
</details>

- Insight: Find all unique host names, which may help with users' seraching for a particular host.

<br/>
5. find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending

- Code
```
let fields = { _id: 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1 }
let filter = { beds: { $gt: 2 }, neighbourhood_cleansed: "Near North Side", review_scores_rating: { $ne: "" } }
let orderBy = { "review_scores_rating": -1 }

db.listings.find(filter, fields).sort(orderBy)
```

<details>

<summary>First Three Results</summary>
[
  {
    name: 'Lux Corner 2BR Downtown- Free Parking - Pool - Gym',
    beds: 3,
    price: '$425.00',
    review_scores_rating: 5
  },
  {
    name: 'LUXURY 3 BR UNIT WITH STUNNING CITY & LAKE VIEWS',
    beds: 4,
    price: '$699.00',
    review_scores_rating: 5
  },
  {
    name: 'Stunning Two Bedroom Duplex at Walton Residence',
    beds: 3,
    price: '$625.00',
    review_scores_rating: 5
  }
]
</details>

- Insight: Find all places with more than two beds in Near North Side, ordered by review scores in descendingly, which may help user to quickly find their places with such specific requirements.

<br/>
6. show the number of listings per host

- Code
```
let countByHost = { $group: { _id: "$host_id", count: { $sum: 1 } } }

db.listings.aggregate([countByHost])
```

<details>

<summary>First Three Results</summary>
[
  { _id: 46734, count: 1 },
  { _id: 17928, count: 1 },
  { _id: 9249272, count: 1 }
]
</details>

- Insight: Find the number of listings for each host, shown by their host_id and count, which may help users who cares about a host's number of listings.

<br/>
7. find the average review_scores_rating per neighborhood, and only show the ones above a 95, sorted in descending order of rating

- Code
```
let filterOutNull = { $match: { "review_scores_rating": { $ne: "" } } }
let avgRatingNeiGroup = { $group: { _id: "$neighbourhood_cleansed", avgRating: {$avg:  "$review_scores_rating" } } }
let above95 = { $match: { avgRating: { $gt: 4.75 } } }
let orderByRating = { $sort: { avgRating: -1 } }

db.listings.aggregate([filterOutNull, avgRatingNeiGroup, above95, orderByRating])
```

<details>

<summary>First Three Results</summary>
[
  { _id: 'Mount Greenwood', avgRating: 4.945 },
  { _id: 'West Lawn', avgRating: 4.931666666666667 },
  { _id: 'Hegewisch', avgRating: 4.92 },
]
</details>

- Insight: Order neighbourhoods with highest average ratings of listings, which may be better for guests to choose to stay during their time at Chicago.