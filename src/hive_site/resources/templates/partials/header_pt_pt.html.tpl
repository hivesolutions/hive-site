<div id="hello-ribbon"></div>
<div id="header-wrapper">
    <div id="menu-content">
        <div id="location-menu">
            <ul>
                <li id="active-location"><a href="language?locale=pt_pt">Português</a></li>
                <li><a href="language?locale=en_us">Inglês</a></li>
            </ul>
        </div>
        <div id="navigation-menu">
            <ul>
                ${if item=area value="home" operator=eq}
                    <li id="active-area"><a href="index">Início</a></li>
                ${else /}
                    <li><a href="index">Início</a></li>
                ${/if}
                ${if item=area value="products" operator=eq}
                    <li id="active-area"><a href="products">Produtos</a></li>
                ${else /}
                    <li><a href="products">Produtos</a></li>
                ${/if}
                ${if item=area value="consulting" operator=eq}
                    <li id="active-area"><a href="consulting">Consultoria</a></li>
                ${else /}
                    <li><a href="consulting">Consultoria</a></li>
                ${/if}
                ${if item=area value="labs" operator=eq}
                    <li id="active-area"><a href="labs">Labs</a></li>
                ${else /}
                    <li><a href="labs">Labs</a></li>
                ${/if}
                ${if item=area value="people" operator=eq}
                    <li id="active-area"><a href="people">Pessoas</a></li>
                ${else /}
                    <li><a href="people">Pessoas</a></li>
                ${/if}
                ${if item=area value="about" operator=eq}
                    <li id="active-area"><a href="about">Sobre</a></li>
                ${else /}
                    <li><a href="about">Sobre</a></li>
                ${/if}
            </ul>
        </div>
    </div>
</div>
<div id="header-shadow"></div>
