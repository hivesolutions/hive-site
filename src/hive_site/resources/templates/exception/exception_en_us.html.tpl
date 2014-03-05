<div id="content">
    <div class="error">
        <div id="media">
            <img src="${out value=base_path /}resources/images/illustration-error.png" height="300" width="900" alt="" />
        </div>
        <h1 class="title">SOMETHING WENT TERRIBLY WRONG</h1>
        <p class="message">${out value=exception_message xml_escape=True /}</p>
    </div>
</div>
