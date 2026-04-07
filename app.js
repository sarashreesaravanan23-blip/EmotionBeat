const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());

// temporary storage (like database)
let students = [];

// simulate async delay
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// GET route
app.get("/students", async (req, res) => {
    await delay(500);
    res.json({ data: students });
});

// POST route
app.post("/students", async (req, res) => {
    await delay(500);

    const student = req.body;
    students.push(student);

    res.json({
        message: "Student added",
        data: student
    });
});

// start server
app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});