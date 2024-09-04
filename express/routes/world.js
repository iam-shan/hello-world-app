const express = require("express")
const router = express.Router()

router.route("/world").get((req, res) => {
    res.status(200).json({message:"World"})
})

module.exports = router