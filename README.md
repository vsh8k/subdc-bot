# subdc-bot
## Python Discord Bot

This is a Python Discord bot that fetches and sends the newest posts from a specified subreddit. It utilizes the Discord bot API and various libraries for functionality.

### Features:

-   Fetches the newest posts from a specified subreddit using the Reddit API.
-   Sends the title and media content (image or video) of the newest post to a designated Discord channel.
-   Supports image and video posts, with fallback options for unsupported media types.

### Dependencies:

-   json: For parsing JSON data.
-   time: Provides timer functionality.
-   pytz: For timezone support.
-   requests: Used for making HTTP requests to retrieve data from the web.
-   discord: Discord bot API library.
-   asyncio: Enables asynchronous programming.

### Usage:

1.  Replace `channel_id` with the actual ID of the Discord channel where you want to send messages.
2.  Set the desired `timeout` value, which defines the delay between checks in minutes.
3.  Replace `subreddit` with the name of the subreddit you want to fetch posts from.
4.  Set up your Discord bot token by replacing `"YOUR_BOT_TOKEN"` with your actual bot token.
