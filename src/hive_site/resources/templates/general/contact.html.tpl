<div id="content">
    <div id="media">
        <img src="${out value=base_path /}resources/images/illustration-contact.png" height="300" width="900" alt="" />
    </div>
    <h1>CONTACT</h1>
    <p>
        Need help navigating the sea of possibilities of recent software technologies? We may be just what you need!
    </p>
    <p>
        We have a very updated and well-prepared team, just waiting to work on that project you were postponing for lack of resources.
        We know just how hard it can be to <b>find, train and keep the right people</b>.
    </p>
    <p>
        Get in touch and learn how you can <b>get the people you want</b>, without breaking the bank.
    </p>
    <p class="form-error" data-current_status="${out value=contact_form_error /}">
        There was an error while sending the information.<br />
        <span class="message">${out value=contact_form_error /}</span>
    </p>
    <form id="contact-form" action="contact#contact-form" method="post">
        <input type="hidden" name="form" value="true" />
        <input type="text" name="contact_form[name]" id="name" value="Your Name" data-original_value="Your Name" data-current_status="${out value=contact_form_model.name /}" data-error="${out value=contact_form_model.validation_errors_map.name /}" />
        <input type="text" name="contact_form[company]" id="company" value="Company Name" data-original_value="Company Name" data-current_status="${out value=contact_form_model.company /}" data-error="${out value=contact_form_model.validation_errors_map.company /}" />
        <input type="text" name="contact_form[email]" id="email" value="Your Email" data-original_value="Your Email" data-current_status="${out value=contact_form_model.email /}" data-error="${out value=contact_form_model.validation_errors_map.email /}" />
        <textarea name="contact_form[problem]" data-original_value="Describe your problem" data-current_status="${out value=contact_form_model.problem /}" data-error="${out value=contact_form_model.validation_errors_map.problem /}">Describe your problem</textarea>
        <a id="send-form-button">Send</a>
    </form>
</div>
