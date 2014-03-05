${include file="partials/doctype.html.tpl" /}
<head>
    <title>${out value=title xml_escape=True /}</title>
    ${include file="partials/content_type.html.tpl" /}
    ${include file="partials/includes.html.tpl" /}
</head>
<body>
    ${include file="partials/header_pt_pt.html.tpl" /}
    <div id="content-wrapper">
        ${include file_value=page_include /}
    </div>
    ${include file="partials/footer_pt_pt.html.tpl" /}
</body>
${include file="partials/end_doctype.html.tpl" /}
