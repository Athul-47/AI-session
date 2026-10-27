const quoteEl = document.getElementById("quote");
const button = document.getElementById("new-quote");
const errorEl = document.getElementById("error");

async function loadQuote() {
  button.disabled = true;
  errorEl.hidden = true;

  try {
    const response = await fetch("/api/quote");
    if (!response.ok) throw new Error("Bad response");
    const data = await response.json();

    quoteEl.textContent = data.quote;
    quoteEl.classList.remove("fade");
    void quoteEl.offsetWidth; // restart the animation
    quoteEl.classList.add("fade");
  } catch (err) {
    errorEl.hidden = false;
  } finally {
    button.disabled = false;
  }
}

button.addEventListener("click", loadQuote);
loadQuote(); // show a quote when the page opens
