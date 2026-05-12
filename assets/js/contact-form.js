/**
 * Contact form: validation, optional Web3Forms (set data-web3forms-key on the form),
 * otherwise opens the user's mail app with a pre-filled message.
 */
(function () {
  "use strict";

  const form = document.getElementById("contact-form");
  if (!form) return;

  const WEB3FORMS_URL = "https://api.web3forms.com/submit";
  const nameEl = form.querySelector("#contact-name");
  const emailEl = form.querySelector("#contact-email");
  const subjectEl = form.querySelector("#contact-subject");
  const messageEl = form.querySelector("#contact-message");
  const countEl = form.querySelector("#contact-message-count");
  const submitBtn = form.querySelector('button[type="submit"]');
  const loadingEl = form.querySelector(".loading");
  const errorEl = form.querySelector(".error-message");
  const sentEl = form.querySelector(".sent-message");

  const limits = {
    name: { min: 2, max: 120 },
    subject: { min: 3, max: 200 },
    message: { min: 10, max: 4000 },
  };

  function showLoading(on) {
    if (on) loadingEl.classList.add("d-block");
    else loadingEl.classList.remove("d-block");
  }

  function showError(msg) {
    errorEl.textContent = msg;
    errorEl.classList.add("d-block");
    sentEl.classList.remove("d-block");
  }

  function clearAlerts() {
    errorEl.classList.remove("d-block");
    sentEl.classList.remove("d-block");
    errorEl.textContent = "";
  }

  function showSuccessWeb3() {
    showLoading(false);
    sentEl.textContent = "Your message has been sent. Thank you!";
    sentEl.classList.add("d-block");
    errorEl.classList.remove("d-block");
    form.reset();
    updateCount();
    if (countEl) countEl.textContent = "0";
    [nameEl, emailEl, subjectEl, messageEl].forEach(function (el) {
      setFieldInvalid(el, false);
    });
  }

  function setFieldInvalid(el, invalid) {
    if (!el) return;
    el.classList.toggle("is-invalid", invalid);
    el.setAttribute("aria-invalid", invalid ? "true" : "false");
  }

  function validEmail(v) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
  }

  function validate() {
    clearAlerts();
    let ok = true;
    const name = nameEl.value.trim();
    const email = emailEl.value.trim();
    const subject = subjectEl.value.trim();
    const message = messageEl.value.trim();

    setFieldInvalid(nameEl, false);
    setFieldInvalid(emailEl, false);
    setFieldInvalid(subjectEl, false);
    setFieldInvalid(messageEl, false);

    if (name.length < limits.name.min || name.length > limits.name.max) {
      setFieldInvalid(nameEl, true);
      ok = false;
    }
    if (!validEmail(email)) {
      setFieldInvalid(emailEl, true);
      ok = false;
    }
    if (subject.length < limits.subject.min || subject.length > limits.subject.max) {
      setFieldInvalid(subjectEl, true);
      ok = false;
    }
    if (message.length < limits.message.min || message.length > limits.message.max) {
      setFieldInvalid(messageEl, true);
      ok = false;
    }

    if (!ok) {
      showError(
        "Please fix the highlighted fields. Message must be at least " +
          limits.message.min +
          " characters."
      );
    }
    return ok;
  }

  function updateCount() {
    if (!countEl || !messageEl) return;
    countEl.textContent = String(messageEl.value.length);
  }

  function buildMailtoUrl() {
    const mailto = (form.dataset.mailto || "tamangsugam09@gmail.com").trim();
    const name = nameEl.value.trim();
    const email = emailEl.value.trim();
    const subject = subjectEl.value.trim();
    const message = messageEl.value.trim();
    const body = "From: " + name + " <" + email + ">\n\n" + message;
    return (
      "mailto:" +
      mailto +
      "?subject=" +
      encodeURIComponent(subject) +
      "&body=" +
      encodeURIComponent(body)
    );
  }

  messageEl.addEventListener("input", updateCount);
  [nameEl, emailEl, subjectEl, messageEl].forEach(function (el) {
    el.addEventListener("input", function () {
      setFieldInvalid(el, false);
    });
  });

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    if (!validate()) return;

    const accessKey = (form.dataset.web3formsKey || "").trim();
    clearAlerts();
    submitBtn.disabled = true;
    showLoading(true);

    try {
      if (accessKey) {
        const res = await fetch(WEB3FORMS_URL, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            access_key: accessKey,
            name: nameEl.value.trim(),
            email: emailEl.value.trim(),
            subject: subjectEl.value.trim(),
            message: messageEl.value.trim(),
            from_name: nameEl.value.trim(),
          }),
        });
        const data = await res.json().catch(function () {
          return {};
        });
        if (data.success) {
          showSuccessWeb3();
        } else {
          showLoading(false);
          showError(data.message || "Could not send. Check your Web3Forms access key or try again.");
        }
      } else {
        showLoading(false);
        sentEl.textContent =
          "Opening your email app with this message ready to send. Send it there to deliver — your text stays here until you send.";
        sentEl.classList.add("d-block");
        errorEl.classList.remove("d-block");
        window.setTimeout(function () {
          window.location.href = buildMailtoUrl();
        }, 250);
      }
    } catch (err) {
      showLoading(false);
      showError("Network error. Check your connection and try again.");
    } finally {
      submitBtn.disabled = false;
    }
  });
})();
