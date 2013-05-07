<html>
    <body>
        <h1>Profile page: ${user.username}</h1>
        <p>username = '${user.username}'</p>
        <p>My pages:</p>
        <ul>
        % for page in pages:
            <li><a href="${page.view_link(request)}">${page.title}</a></li>
        % endfor
        </ul>
    </body>
</html>
