
function setDarkMode() {
    document.body.classList.remove("light-mode");
    document.body.classList.add("dark-mode");
    localStorage.setItem("theme", "dark");

    // Mengubah kelas elemen pada tabel
    const main_nav = document.getElementById("main_nav");
    const modeLightDark = document.getElementById("button_light_dark");
    const table_1 = document.getElementById("table_1");
    const table_2 = document.getElementById("table_2");
    const lamp_icon = document.getElementById("button_lamp");
    const body = document.getElementById("body");
    table_1.classList.add("table-dark"); // Tambahkan kelas Dark Mode
    table_2.classList.add("table-dark");
    body.innerHTML = `body {margin: 0; height: 100vh; background-image: linear-gradient(to bottom, #125865, #93817d); 
        background-attachment: fixed; background-size: cover; background-repeat: no-repeat;
        }     
        .btn-lamp-dark {
            background: transparent;
            border: none;
            color: white;
        }
        .btn-lamp-light {
            background: transparent;
            border: none;
            color: black;
        }
        .footer {
            background-color: blue;
        }`;
    modeLightDark.classList.remove("btn-lamp-light");
    modeLightDark.classList.add("btn-lamp-dark");
    modeLightDark.style.color = "#fff";
    main_nav.classList.add("navbar-dark");
    main_nav.style.backgroundColor = "#125871"
    lamp_icon.style.fill = "white";
    


}
function setLightMode() {
    document.body.classList.remove("dark-mode");
    document.body.classList.add("light-mode");
    localStorage.setItem("theme", "light");


    // Mengubah kelas elemen pada tabel
    const main_nav = document.getElementById("main_nav");
    const modeLightDark = document.getElementById("button_light_dark");
    const table_1 = document.getElementById("table_1");
    const table_2 = document.getElementById("table_2");
    const lamp_icon = document.getElementById("button_lamp");
    const body = document.getElementById("body");
    table_1.classList.remove("table-dark"); 
    table_2.classList.remove("table-dark");
    body.innerHTML = `body { background-image: url("static/images/Background.png"); background-color: #fff; background-repeat: no-repeat; background-size: cover;} 

    .btn-lamp-dark {
        background: transparent;
        border: none;
        color: white;
    }
    .btn-lamp-light {
        background: transparent;
        border: none;
        color: black;
    }
    .footer {
        background-color: blue;
    }`;
    modeLightDark.classList.remove("btn-lamp-dark");
    modeLightDark.classList.add("btn-lamp-light");
    main_nav.classList.remove("navbar-dark");
    main_nav.style.backgroundColor = "rgba(32, 165, 195,0.2)";
    main_nav.style.backdropFilter = "blur(10px)";
    lamp_icon.style.fill = "black";


}
    // Fungsi untuk memeriksa preferensi tema di Local Storage saat halaman dimuat
function checkThemePreference() {
    const theme = localStorage.getItem("theme");
    if (theme === "dark") {
        setDarkMode(); // Jika tema yang disimpan adalah "dark", atur ke Dark Mode
    } else {
        setLightMode(); // Jika tidak, atur ke Light Mode
    }
}
function setMode() {
    
    const theme = localStorage.getItem("theme");
    if (theme === "dark") {
        setLightMode(); // Jika tema yang disimpan adalah "dark", atur ke Dark Mode
    } else {
        setDarkMode(); // Jika tidak, atur ke Light Mode
    }

}

// Panggil fungsi checkThemePreference saat halaman dimuat
window.onload = checkThemePreference;
