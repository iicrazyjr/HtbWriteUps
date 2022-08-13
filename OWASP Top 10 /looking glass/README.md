
# Looking glass challenge

In this challenge we are going to abuse of command injection


## How we are going to exploit


To get an idea of what happens in this challenge, we will have to analyse the function of the page, in this case it is in charge of performing 'ping' and 'traceroute' commands, so we can imagine that the web is using these utilities through a php script.

Then, since ping and traceroute are being used via bash, we can try to inject commands in the following way.

```php
system("ping" + host);
```

So we can inject code like this

```php
system("ping" + host; whoami);
```

Once we have some idea of how the web works, we can intercept the request being made, using burpsuite for example, and analyse the parameters being sent to the server.

Here is the python code I have written to automate this challenge

[code](https://github.com/iicrazyjr/HtbWriteUps/blob/main/OWASP%20Top%2010%20/looking%20glass/glass.py)
## Documentation

[Code injection documentation](https://owasp.org/www-community/attacks/Code_Injection)

