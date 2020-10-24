# [Town Deals](https://town-deals.herokuapp.com/)
Ecommerce platform dedicated to purchase of used, local products. Add-to-Cart and Checkout options
available to guest users. Name, email, and shipping information required. Login and Account creation not a requirement.

* Built the backend using Django in Python. Created an app in the project dedicated to flow of data from the frontend to the database and
back through URLs parameters and JSON data.
* Deployed the frontend in JavaScript, HTML, and CSS. Served JavaScript and CSS as static files. Passed HTML as templates to the the frontend 
through URL routes in Django.
* Initialized a database using PostgreSQL. Stored customer data, product data, order history for each customer, and shipping information for each customer.
Utilized relational database paradigm linking ordered items to respective orders and orders to respective customers through Foreign Keys in Django Models

### External Tech

* Deployed the website on Heroku and stored project credentials inside Heroku's configuration variables.
* Hosted images(product images), CSS, and JavaScript as static files in S3 Buckets provided by AWS.
* Configured pgAdmin facilitating systematic visualisation and management of the PostgreSQL database.
* Hosted the database on AWS RDS as a live database migrating from the locally available SQLite3 provided by Django.   
<br>
<p align="center">
  <img src="https://github.com/abhigya-ps/town-deals/blob/main/images/towndeals_images.JPG" alt="demo_store" width="60%" align="center">
</p>
