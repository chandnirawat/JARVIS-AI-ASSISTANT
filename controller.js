$(document).ready(function () {

    if (window.controllerLoaded) return;
    window.controllerLoaded = true;

    // =========================
    // Display speak message from Python
    // =========================
    eel.expose(displaymessage);
    function displaymessage(message) {
        $(".siri-message").text(message);   
        if ($.fn.textillate) {
            $('.siri-message').textillate('start');
        }
    }

    // =========================
    // Show Hood (UI element)
    // =========================
    eel.expose(showHood);
    function showHood() {
        $("#oval").show();        
        $("#siriwave").hide();    
    }

    // =========================
    // Mic Button Click Listener
    // =========================
    $("#mic-btn").click(async function() {
        startSiriWave(); // show wave animation
        try {
            await eel.start_listening()();  // call Python mic function
        } catch (err) {
            console.error("Eel call error:", err);
        } finally {
            stopSiriWave();  // stop wave after command executes
        }
    });

    // =========================
    // Siri Wave Start
    // =========================
    function startSiriWave() {
        $(".siri-message").text("Listening...");
        if ($.fn.textillate) {
            $(".siri-message").textillate('stop');
            $(".siri-message").textillate({
                in: { effect: 'fadeIn' },
                loop: true
            });
        }
        $("#siriwave").show(); // show wave element
        $("#oval").hide();
    }

    // =========================
    // Siri Wave Stop
    // =========================
    function stopSiriWave() {
        if ($.fn.textillate) {
            $(".siri-message").textillate('stop');
        }
        $(".siri-message").text("");
        $("#siriwave").hide();
        $("#oval").show();
    }

});