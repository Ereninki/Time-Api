# Time Api

This is a local api that i made because im making an oled desk thingy and all the time apis had rate limits so i made mine with no rate limit if you have the api key to use it

# Usage

it has 2 endpoint called `/api/v1/time` and /api/v1/date` with 2 required parameter, **api_key** and **timezone.**

For **timezone** you just type smth like **Europe/Amsterdam** or **Europe/Istanbul.**
For **api_key** you need set it **yourself**, just open **.env.example** put a password there (it could be anything) and change file name to **.env** and thats it. Now when youre making a request to **/api/v1/time** or **/api/v1/date** you just put your timezone and your api_key!!

**Examples:**
`https://time-api.ereninki.hackclub.app/api/v1/time?timezone=Europe/Istanbul&api_key=<api key>`
`https://time-api.ereninki.hackclub.app/api/v1/date?timezone=Europe/Istanbul&api_key=<api key>`

---

# Local Running

if you want to locally run this, you need [uv](https://docs.astral.sh/uv/#installation) installed on your computer, then you need to clone this project with `git clone https://github.com/Ereninki/Time-Api` and run this command in the directory with the instructions in **# Usage** `uv run ./main.py` and with that, now you can make requests to your api!!
