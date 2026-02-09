changeTheme()


let themeBtn = document.querySelector(".btn_change_theme")

themeBtn.addEventListener("click" , () => {
    console.log("themeBtn", themeBtn.textContent)
    if (themeBtn.textContent === "🔆") {
        localStorage.setItem("theme", "light")
        document.querySelectorAll(".btn_change_theme").forEach(element => {
            element.textContent = "🌙"
            changeTheme()
        })

    } else if (themeBtn.textContent === "🌙") {
        localStorage.setItem("theme", "dark")
        document.querySelectorAll(".btn_change_theme").forEach(element => {
            element.textContent = "🔆"
            changeTheme()
        })
    }
    })



function changeTheme() {
    console.log("changeTheme() ex")
if (localStorage.getItem("theme") === false) {
    localStorage.setItem("theme", "dark")
}

else if (localStorage.getItem("theme") === "dark") {
    document.querySelectorAll(".btn_change_theme").forEach(element => {
            element.textContent = "🔆"
        })

        document.body.style.backgroundColor = "rgb(33, 30, 30)"
        document.body.style.color = "aliceblue"
        document.querySelectorAll(".task").forEach(task => {
            task.style.backgroundColor = "rgb(37, 34, 34)"
        })
        document.querySelectorAll(".completed_task").forEach(completed_task => {
            completed_task.style.backgroundColor = "rgb(37, 34, 34)"
        })
}

else if (localStorage.getItem("theme") === "light") {
    document.querySelectorAll(".btn_change_theme").forEach(element => {
            element.textContent = "🌙"
        })

        document.body.style.backgroundColor = "aliceblue"
        document.body.style.color = "black"
        document.querySelectorAll(".task").forEach(task => {
            task.style.backgroundColor = "#dde4ec"
        })
        document.querySelectorAll(".completed_task").forEach(completed_task => {
            completed_task.style.backgroundColor = "#dde4ec"
        })
}
}
