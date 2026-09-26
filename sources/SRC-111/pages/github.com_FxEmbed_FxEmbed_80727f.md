source: https://github.com/FxEmbed/FxEmbed

FxEmbed is a Cloudflare Worker, so the Docker image runs the local Workers runtime through Wrangler rather than starting a plain Node.js server. The image uses `node:24-bookworm-slim`

because Wrangler's `workerd`

binary is glibc-linked and does not run reliably on Alpine/musl.

Before building, copy and edit the local configuration files if you need custom domains, branding, or credentials:

```
cp .env.example .env
cp wrangler.example.toml wrangler.toml
cp branding.example.json branding.json
```

Build and run with Docker Compose:

`docker compose up -d --build`

The worker listens on `http://localhost:8787`

. Because FxEmbed routes by the `Host`

header, test a specific realm like this:

`curl -H "Host: fxtwitter.com" -H "User-Agent: Discordbot/2.0" "http://localhost:8787/user/status/123"`

You can also open `http://localhost:8787/`

without a `Host`

header to see the local realm prefixes.

Environment variables from `.env`

are bundled during the Docker build, so rebuild the image after changing domain lists or other build-time configuration:

`docker compose up -d --build`

Runtime secrets such as `CREDENTIAL_KEY`

and `EXCEPTION_DISCORD_WEBHOOK`

can be supplied through your shell or Compose `.env`

file. Stop the service with:

`docker compose down`

**Licensed under the permissive MIT license. Feel free to send a pull request!**


Feel free to [open an issue](https://github.com/FxEmbed/FxEmbed/issues)

[Mosaic](https://github.com/FxEmbed/mosaic) Multi-image combiner by [Antonio32A](https://github.com/Antonio32A) and improved by [Syfaro](https://github.com/Syfaro), [Deer Spangle](https://github.com/Deer-Spangle), and [dangered wolf](https://github.com/dangeredwolf)

[Everyone else who has contributed to the main project!](https://github.com/FxEmbed/FxEmbed/graphs/contributors)

Twitter, Tweet, and X are trademarks of X Corp. This project is not affiliated in any way with X Corp or Twitter.