//Register the service worker when the page loads
if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("static/js/serviceworker.js")
            .then(() => console.log("LiftLog service worker registered"))
            .catch((err) => console.log("Service worker failed:", err));
    });
}