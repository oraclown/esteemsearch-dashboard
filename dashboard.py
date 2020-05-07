import streamlit as st 

from queries import search, get_status


def format_results(lis):
    for i, r in enumerate(lis):
        content = ''
        edit = st.checkbox(r['title'], key=i)
        st.text('author: ' + r['author'] + ' ' + str(r['author_rep']))
        display = st.empty()
        content = display.markdown(r['body'])
        if not edit:
            display.empty()


st.title('esteem search dashboard')

query = st.text_input('enter a search query')
if query:
    r = search(query)
    format_results(r['results'])

if st.button('get api key status'):
    r = get_status()
    st.write(f"You have {r['request_limit'] - r['request_count']} requests left.")


# {
#   "took": 0.062,
#   "hits": 2,
#   "results": [
#     {
#       "id": 49194954,
#       "author": "good-karma",
#       "permlink": "esteem-surfer-1-0-0-release-79775e065812d",
#       "category": "esteem",
#       "children": 500,
#       "author_rep": 76.26,
#       "title": "eSteem: Surfer 1.0.0 Release",
#       "title_marked": "<mark>eSteem</mark>: <mark>Surfer</mark> 1.0.0 Release",
#       "body": "Yay! We've just released our desktop client for Steem! After few months of development, we are really happy with current state of the Surfer and decided to roll out initial beta version for you guys to test out. Release is available for Windows, Mac OS and Linux operating systems whichever one you use, you can try it out now.\n\n![surfer-release-3-color2.png](https://steemitimages.com/DQmSeTG5RLTP7AR5Km9mfNEsx8EQ2GapFVeTupZY474M3Tj/surfer-release-3-color2.png)\n\nBasically it's the Steem interface you get used to but with additional handy options. Everything works out faster and easier with **Surfer**. You can create your posts, surf your friends feed or trending/hot/etc pages, upvote what you like, write comments, read replies, do all major Steem functions in your daily social surfing as well as wallet actions and of course few extras: search, discover different tags etc.\n\n### Meet the eSteem Surfer\n\n![trending.png](https://steemitimages.com/DQmVwFfYThpmTNoMBSHjq69HyzRmiHdd7HEJGuvyuUvCMZ7/trending.png)\n\n![wallet.png](https://steemitimages.com/DQmTPWzizQTjP25ZhqXrsQV9i4mtVJaN3fv3yJChKoYNzVz/wallet.png)\n\n### Why Surfer\n\nAs you may know we have eSteem Mobile application in your finger tips with support for both Android and iOS. Our users love flexibility and many have requested desktop app for long time. So Surfer was born to give you extra boost with both mobile as well as desktop experiences, once you logged in, your drafts, bookmarks, images are seemlessly synced in... Our hope is that eSteem Surfer will make your Steem Surfing experiences much better.\n\n### Drafts\n\nStart writing a post on your computer and continue on the go with eSteem Mobile available for Android and iOS. You can save any amount of drafts. And it works both ways, your images are also available in your image Gallery.\n\n### Post Scheduling\n\nProbably one of the best features for top bloggers is to plan everything and prepare for the future. Just choose exact date and time for any of your drafts and relax. You don't have to make reminders anymore.\n\n![post_edit.png](https://steemitimages.com/DQmYD8ju39r59sL1DPLiKypDneHiLAYHr9pAwvQoHPD2WTo/post_edit.png)\n\n### Favorites & Bookmarks\n\nYou can add any account to Favorites for quick access to them or simply search for them later on. Also there is an ability to Bookmark any post so you will never loose interesting posts. And the most great thing is that all those goodies are automatically synced across mobile and desktop devices you have.\n\n![favorites.png](https://steemitimages.com/DQmPYjefnWzdeX4bUBWSiPTChG7jTyFvt5dpeY5UUmAgrwb/favorites.png)\n\n### Multi-accounts\n\nYou can log in to as many accounts as you want and switch in between them in a couple of clicks. Loggin in supports both Steemconnect as well as traditional authentication.\n\n### Is it safe and secure to use my password there?\n\nYour password is stored locally on your machine and never leave your device. eSteem Surfer is open source, so the code is open for the review and we would be really happy to get any contribution into the code (bug fixes, tweaks and new functions, reviews).\n\nPlus all your keys are encrypted on your device with PIN code. PIN setup secures app from unwanted eyes as well, so you don't have to log out from the app too often. If there is physical access to your computer by your kids for example, everything stays safe.\n\n![pin.png](https://steemitimages.com/DQmQE7JtpL6bpNrmSyVu1HNvL95dA3v52Qbx5vJogRWXNwv/pin.png)\n\n\n### Token Exchange\n\nYou can quickly see the whole STEEM/BTC and SBD/BTC graphics from Bittrex, Binance right inside the app. Handy? Token exchange page will receive many more improvements in upcoming releases. And we have big plans for this particular page, stay tuned!\n\n![bittrex.png](https://steemitimages.com/DQmfGvCGv8m67QkDReCb3NTZSeRanCRQc5fcHiByZ4ECyCs/bittrex.png)\n\n### Wallet\n\nWallet page has many improvements and includes escrow transfers, advanced power up/down. Future releases will include some more additions like delegations, etc.\n\n### Discover\n\nDiscover page gives you ability to find new authors and start following them. \n\n### Activities\n\nSame feature from eSteem Mobile, has been added to Surfer. Where you can check activities for your account. We are in process of improving this and add push notifications right on your desktop.\n\n### Settings\n\nFlexibility is the key on decentralized network, same feature our users love about eSteem Mobile has been added, support for custom server selection.\n\n### Editor and more\n\nAnd of course, beautiful and simple editor to write your blogs. Comments are paginated to help you manage window space, informative profile page, surf through each account's feed, edit account details and improved search functionality, you can even paste steemit/busy links there to open it up and many more features, let us know which one surprised you most. :)\n\n\nWe are planning to add new functions and would be glad if you test our current release. Detailed comments related to bugs, feature suggestions or any other improvements of **eSteem Surfer** would be appreciated!\n\n## Download\n\nDownload from [Github](https://github.com/eSteemApp/esteem-surfer/releases): https://github.com/eSteemApp/esteem-surfer/releases/tag/1.0.0\n\n`exe` file for **Windows** users\n\n`dmg` file for **Mac** users\n\n`deb` and `rpm` file for **Linux** users\n\n**Source code:** https://github.com/eSteemApp/esteem-surfer\n**Report bugs:** https://github.com/eSteemApp/esteem-surfer/issues\n\n![sticker.png](https://steemitimages.com/DQmU9yczk1NnipwNkq86nsnK3TNAGFTDCNUxLbWaenLeN45/sticker.png)\n\n\n### Steem on! Surf on!\n\n---\n\n-   Email: `info@esteem.app`\n-   Home: [https://esteem.app](https://esteem.app/ \"This link will take you away from esteem\")\n-   Github: [https://github.com/esteemapp](https://github.com/esteemapp \"This link will take you away from esteem\")\n-   Telegram: [https://t.me/esteemapp](https://t.me/esteemapp \"This link will take you away from esteem\")\n-   Discord: [https://discord.gg/9cdhjc7](https://discord.gg/9cdhjc7 \"This link will take you away from esteem\")\n\n---\n\n##### <center>[vote witness](https://steemit.com/~witnesses) `good-karma`</center>",
#       "body_marked": "/github.com/eSteemApp/<mark>esteem</mark>-<mark>surfer</mark>\nReport bugs: https://github.com/eSteemApp/<mark>esteem</mark>-<mark>surfer</mark>/issues\n\n\n\nSteem on!",
#       "img_url": "https://steemitimages.com/DQmSeTG5RLTP7AR5Km9mfNEsx8EQ2GapFVeTupZY474M3Tj/surfer-release-3-color2.png",
#       "payout": 955.15,
#       "total_votes": 2082,
#       "up_votes": 2082,
#       "created_at": "2018-05-18T19:31:21+00:00",
#       "tags": [
#         "esteem",
#         "surfer",
#         "desktop",
#         "wallet",
#         "steem"
#       ],
#       "app": "esteem/1.0.0-surfer",
#       "depth": 0
#     },
#     {
#       "id": 48071951,
#       "author": "good-karma",
#       "permlink": "upcoming-esteem-surfer-b911ad82fc8ef",
#       "category": "esteem",
#       "children": 126,
#       "author_rep": 76.26,
#       "title": "Upcoming eSteem Surfer",
#       "title_marked": "Upcoming <mark>eSteem</mark> <mark>Surfer</mark>",
#       "body": "![esteem_surfer_cover_preview.png](https://steemitimages.com/DQmb8YLC9RUjo6VmDzPs359SViJEXnZXF6JhwYfKYQKurPB/esteem_surfer_cover_preview.png)\n\nThese days we are still working hard on **eSteem Surfer** Steem Desktop application. We had been talking about it on London Cryptocurrency Show recently. Our Github repo is private for now and this is still WIP (work in progress) but we are almost ready for public release.\n\n### Sneak Peek\n\nAfter our internal alpha testing we will make an open beta release. While you are waiting just check few screens to get a clue on how it will look like. A lot has been done and much more of to come and some parts you see in screenshots might change anytime until release.\n\nDesktop version will include all the functions you like in eSteem Mobile such as push notifications, activity center, drafts, post scheduling, favorites, bookmarks, image gallery and more.\n\n![profile.png](https://steemitimages.com/DQmW4hUa7JK5yPNSd81BmMjXTrCXeXuQsnRKE7Anwc9paGB/profile.png)\n\n![post.png](https://steemitimages.com/DQmPFBQm89owaVeAv9bpPpS3F7A182R5rofWnUDqsHV4PPM/post.png)\n\n### Major features are already in place:\n\n- All the feeds surfing like your friends, trending, hot, etc\n- New post creation\n- Commenting\n- Upvoting\n- Wallet & transfers, escrow\n- User profile stats\n- Replies\n- Bookmarks, Drafts, Image gallery, Favorites synced with eSteem Mobile\n\nSurfer will support Windows/Mac/Linux users, just like mobile version is on major platforms for those who adore their mobiles keeping connection with your Steem fellas via small boxes with screens, Surfer will be same but for much bigger screens and different operation systems.\n\nWe will appreciate any comments, feature requests, user interface suggestions. We are looking for new talents by the way, reach out via email if you are interested!\n\n---\n\n-   Email: `info@esteem.app`\n-   Home: [https://esteem.app](https://esteem.app/ \"This link will take you away from esteem\")\n-   Github: [https://github.com/esteemapp](https://github.com/esteemapp \"This link will take you away from esteem\")\n-   Telegram: [https://t.me/esteemapp](https://t.me/esteemapp \"This link will take you away from esteem\")\n-   Discord: [https://discord.gg/an8Tj6H](https://discord.gg/an8Tj6H \"This link will take you away from esteem\")\n\n---\n\n##### <center>[vote witness](https://steemit.com/~witnesses) `good-karma`</center>",
#       "body_marked": "surfercover_preview.png\" />\n\nThese days we are still working hard on <mark>eSteem</mark> <mark>Surfer</mark> Steem Desktop application. We had been talking about it on London Cryptocurrency Show recently.",
#       "img_url": "https://steemitimages.com/DQmb8YLC9RUjo6VmDzPs359SViJEXnZXF6JhwYfKYQKurPB/esteem_surfer_cover_preview.png",
#       "payout": 63.086,
#       "total_votes": 848,
#       "up_votes": 848,
#       "created_at": "2018-05-11T17:37:15+00:00",
#       "tags": [
#         "esteem",
#         "esteem-surfer",
#         "desktop",
#         "wallet",
#         "steem"
#       ],
#       "app": "esteem/1.6.0",
#       "depth": 0
#     }
#   ]
# }