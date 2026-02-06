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

        //document.getElementById("btn_update_in_update_form").style.backgroundColor = "black"
}
}



// надо - что бы при входе проверялся local storage и если там есть что то то делал:
//      если dark то ставит темные цвета и btn = 🔆, если light то светлые и btn = 🌙
// если local storage не создан, то создать и записать туда светлую тему

// при нажатие кнопки - если был 🔆 станет 🌙 и local storage перепишется на light и так же в обратную сторану
