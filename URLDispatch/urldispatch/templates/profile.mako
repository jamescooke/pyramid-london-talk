<html>
    <body>
        <h1>Profile page: ${user.username}</h1>
        <p>username = '${user.username}'</p>
        <p>My pages:</p>
        <ul>
        % for page in pages:
            <li><a href="${request.route_path('page', username=user.username, page_title=page.title.lower())}">${page.title}</a></li>
        % endfor
        </ul>
    </body>
</html>
