<div id="hello-ribbon"></div>
<div id="header-wrapper">
    <div id="menu-content">
        <div id="location-menu">
            <ul>
                <li><a href="language?locale=pt_pt">Portuguese</a></li>
                <li id="active-location"><a href="language?locale=en_us">English</a></li>
            </ul>
        </div>
        <div id="navigation-menu">
            <ul>
                ${if item=area value="home" operator=eq}
                    <li id="active-area"><a href="index">Home</a></li>
                ${else /}
                    <li><a href="index">Home</a></li>
                ${/if}
                ${if item=area value="products" operator=eq}
                    <li id="active-area"><a href="products">Products</a></li>
                ${else /}
                    <li><a href="products">Products</a></li>
                ${/if}
                ${if item=area value="consulting" operator=eq}
                    <li id="active-area"><a href="consulting">Consulting</a></li>
                ${else /}
                    <li><a href="consulting">Consulting</a></li>
                ${/if}
                ${if item=area value="labs" operator=eq}
                    <li id="active-area"><a href="labs">Labs</a></li>
                ${else /}
                    <li><a href="labs">Labs</a></li>
                ${/if}
                ${if item=area value="people" operator=eq}
                    <li id="active-area"><a href="people">People</a></li>
                ${else /}
                    <li><a href="people">People</a></li>
                ${/if}
                ${if item=area value="about" operator=eq}
                    <li id="active-area"><a href="about">About</a></li>
                ${else /}
                    <li><a href="about">About</a></li>
                ${/if}
            </ul>
        </div>
    </div>
</div>
<div id="header-shadow"></div>
