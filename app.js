
const express =require("express")
const app= express()
const createTables= require("./database/createUserTable")
const bcrypt = require('bcrypt');
const jwt=require("jsonwebtoken")
const pool=require("./config/db")
const axios = require("axios");
const FormData = require("form-data");
const fs = require("fs");
const cookieParser = require("cookie-parser");


const saltRounds = 10;
app.use(express.json())
app.use(express.urlencoded({extended:true}))

app.use(cookieParser())
//app.use(express.static(Path.json(__dirname,"public")))


createTables()

//configure multer
const multer = require("multer");

const upload = multer({
    dest: "uploads/"
});

app.set("view engine", "ejs")
app.get("/",(req,resp)=>{

    resp.render("login")
})
app.get("/signin",(req,resp)=>{
    resp.render("signin")
})

app.post("/login", async (req, res) => {
    const { email, password } = req.body;

    // Find user
    const result = await pool.query(
        "SELECT * FROM users WHERE email = $1",
        [email]
    );

    if (result.rows.length === 0) {
        return res.send("Email or Password is Invalid! Please try again");
    }

    const user = result.rows[0];

    // Compare password
    const isMatch = await bcrypt.compare(password, user.password);

    if (!isMatch) {
        return res.send("Email or Password is Invalid! Please try again");
    }

    // Generate JWT
    const token = jwt.sign(
        {
            id: user.id,
            email: user.email,
            username: user.username
        },
        "secret"
    );

    res.cookie("token", token);

    res.render("chatter",answer=null);
  });



app.post("/signin", async (req, resp) => {

    const { name, email, password, confirmPassword } = req.body;

    if (password !== confirmPassword) {
        return resp.send("Passwords do not match");
    }

    const result = await pool.query(
        "SELECT * FROM users WHERE email = $1",
        [email]
    );

    if (result.rows.length > 0) {
        return resp.send("User already exists");
    }

    const hash = await bcrypt.hash(password, 10);

    await pool.query(
        `INSERT INTO users(username, email, password)
         VALUES($1, $2, $3)`,
        [name, email, hash]
    );

    const token = jwt.sign(
        { email, name },
        "secret"
    );

    resp.cookie("token", token);
    resp.render("chatter",answer=null);
    
   });

app.post("/logout", (req, res) => {
    res.clearCookie("token");
    res.redirect("/");
  });

app.post("/upload", upload.single("pdf"), async (req, res) => {

    console.log("req.file =", req.file);
    console.log("req.body =", req.body);
    try {

        // Create a new multipart form
        const form = new FormData();

        // Add the uploaded PDF
        form.append(
            "pdf",
            fs.createReadStream(req.file.path)
        );

        // Add the user's question
        form.append(
            "question",
            req.body.question
        );

        // Send both to the FastAPI server
        const response = await axios.post(
            "http://127.0.0.1:8000/ask",
            form,
            {
                headers: form.getHeaders() 
            }
        );

        // Get the answer returned by FastAPI
        const answer = response.data.answer;

        // Render the answer on your EJS page
        res.render("chatter", {
            answer: answer
        });

    } catch (error) {
        console.error(error);
        res.send("Error communicating with FastAPI");
    }
});


app.listen(80,()=>{
    console.log("Server is running...")
})

