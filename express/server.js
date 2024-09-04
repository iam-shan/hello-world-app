const express = require("express")

const app = express()

const worldRouter = require("./routes/world")

app.use(worldRouter)
app.listen(3000)