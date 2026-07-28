//const { Pool } = require("pg");  // extract only pool property of the pg
const pg = require("pg");
require("dotenv").config();  //Its job is to load the variables from your .env file into process.env.

const pool = new pg.Pool({
    connectionString: process.env.DATABASE_CONNECTION_URL,
    ssl: {
        rejectUnauthorized: false
    }
});

module.exports = pool;
