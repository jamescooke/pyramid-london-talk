<html>
    <body>
        <h1>Welcome to PyramidPress</h1>
        <p>We have lots of users for you to look at:</p>
        <ul>
            % for u in users:
                <li><a href="${request.route_path('profile', username=u.username)}">${u.username}</a></li>
            % endfor
        </ul>
    </body>
</html>
