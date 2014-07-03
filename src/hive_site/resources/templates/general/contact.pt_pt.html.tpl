<div id="content">
    <div id="media">
        <img src="${out value=base_path /}resources/images/illustration-contact.png" height="300" width="900" alt="" />
    </div>
    <h1>CONTACTO</h1>
    <p>
        Precisa de ajuda a navegar o mar de possibilidades oferecidas pelas novas tecnologias? Podemos ser justamente aquilo que precisa!
    </p>
    <p>
        Temos uma equipa actualizada e preparada, ansiosa por trabalhar naquele projecto que tem adiado por falta de recursos ou disponibilidade.
        Sabemos quão difícil pode ser <b>encontrar, treinar e manter as pessoas certas</b>.
    </p>
    <p>
        Contacte-nos e obtenha as <b>pessoas que procura</b>, dentro do seu orçamento.
    </p>
    <p class="form-error" data-current_status="${out value=contact_form_error /}">
        Ocorreu um erro ao enviar a informação.<br />
        <span class="message">${out value=contact_form_error /}</span>
    </p>
    <form id="contact-form" action="contact#contact-form" method="post">
        <input type="hidden" name="form" value="true" />
        <input type="text" name="contact_form[name]" id="name" value="O Seu Nome" data-original_value="O Seu Nome"
               data-current_status="${out value=contact_form.name /}" data-error="${out value=contact_form.validation_errors_map.name /}" />
        <input type="text" name="contact_form[company]" id="company" value="Nome da Empresa" data-original_value="Nome da Empresa"
               data-current_status="${out value=contact_form.company /}" data-error="${out value=contact_form.validation_errors_map.company /}" />
        <input type="text" name="contact_form[email]" id="email" value="O Seu Email" data-original_value="O Seu Email"
               data-current_status="${out value=contact_form.email /}" data-error="${out value=contact_form.validation_errors_map.email /}" />
        <textarea name="contact_form[problem]" data-original_value="Descreva o seu problema" data-current_status="${out value=contact_form.problem /}"
                  data-error="${out value=contact_form.validation_errors_map.email /}">Descreva o seu problema</textarea>
        <a id="send-form-button">Enviar</a>
    </form>
</div>
