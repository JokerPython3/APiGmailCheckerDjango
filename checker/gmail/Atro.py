import requests
import http.client
from user_agent import generate_user_agent
import random

class GmailChecker:
    def __init__(self,email):
        self.email = email
        self.agent = str(generate_user_agent())
        self.client = requests.session()
        if "@" in self.email:self.email= self.email.split("@")[0]
    def __str__(self):


        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
            'priority': 'u=0, i',
            'referer': 'https://accounts.google.com/',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

        }

        params = {
            'biz': 'false',
            'continue': 'https://www.google.com/',

            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'hl': 'en',

        }

        response = self.client.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        try:
            s1 = response.text.split('"Qzxixc":"')[1].split('"')[0]
            tl = response.url.split("TL=")[1]

            at = response.text.split('"SNlM0e":"')[1].split('"')[0]

            headers = {
                'accept': '*/*',
                'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'priority': 'u=1, i',
                'referer': 'https://accounts.google.com/',

                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
                'x-same-domain': '1',

            }

            params = {
                'rpcids': 'E815hb',
                'source-path': '/lifecycle/steps/signup/name',

                'hl': 'en',
                'TL': tl,
            }
            name = "".join(random.choice("qwertyuiuopasdfghjklzxcvbnm") for i in range(random.randrange(5, 9)))
            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(
                name, at)

            response = self.client.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,

                headers=headers,
                data=data,
            )
            headers = {
                'accept': '*/*',
                'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'priority': 'u=1, i',
                'referer': 'https://accounts.google.com/',

                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
                'x-same-domain': '1',
            }

            params = {
                'rpcids': 'eOY7Bb',
                'source-path': '/lifecycle/steps/signup/birthdaygender',

                'hl': 'en',
                'TL': tl,

            }

            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C2%2Cnull%2Cnull%2Cnull%2C%5C%22%3CHtJq0ooCAAbV1vff9daN6IX1Fmilur_0ADQBEArZ1JW_Bzhtkn_WqleJ_cL80Z-ocP5sTDowp2Xen-18mGPAqD4ffVrkQ_t9mkz7KraPzQAAAj6dAAAAIqcBB7EATbzTbvA3cPQkojybX5bViKQROnFcfdDhrhl-jmmWphs7JMeslHuIV50hPhrghyLTAbCUjDodpfNO-jq6dqdszmHqA1JVU-svBEyEWeBQVg9VqwDhZI07j98LD9fcej2btqNmVKiC9BhP_vR1HPd_zUtQJGdDrlkd8TzAZx3AZvPhmnyag2QDUZfc6YK7Ta-eoRx9_ixOdwjgnd17L2TMNQLqxBMI8ChxxJVT3-YbPjY0CkyofH1l1UsGhWuVxAh0rMyZ97t-kz69CtE9rAuUwwBVaMQIWF5QX1A9Gpv3RyC2dz2LEJGP6fIolu4ZAU0amwdi5lvbduq8mQHaKYMxNtftOl4mP9rfFYAs1TgoqJ649VllWLYPkRfBHCFSqvCShZsiRN-dme9q7NCgcIoO8ixnPWL18FNEcSX-kP9zNM0QF-aTxCGykF7DMISIFD3N5-PwdNaKklLiIEe7JNgM4Ti3bl5s17vyY8wDNxmdXRnYDoeoLMQbi4By9jBhRS8_UvcaNaonXcuk_kZ4zTwY8H3d9Tjkn4fuXcaiH9FEoybOcbk08l1b-rcPx31Umw2yWoB4xmXBVE1OtRWoP2soa9TF4D3DKin0nYLHcWaumIoH-TI8q5UKnSxXA6XrdsEJPyrgxC0TcARC5gGcsg1LjxcnqZWu2K59-aJO8unc1lP2SDKluTPA1dz9bOe9upZrpCgFm9jiba9Pk0q40U1oF-z1a6oNYysfECfEEvtVSndHWWasFH04ETSXsN62fZC-NW5AFqEpg2_z772G0tspGEw3e_935eijy5pEk-9rwzF_eWgS2_QJ7xNjwrGFy3_GkafjDyzO8Dx_xdLK4WIY707VLtmMc93Dx6ko9bVWZmEVz3KYRuMMt__wJce7_16RM4taLQp_iD1cCh4ROimmwzVu3_wIS9AayI9SABnJS0vSse2jE5SleN5Uw4FvaijD-_p01imq887t4_jnpvKLzsQvv4tFYhY0LvP32Y3xLgEh6DI25aDXXgMEnMg0AOxxlAyviNAPFdB4bu-O3rU_egPPhrojfscB9a6G3VtYXt0El6CyBKZ3_aos3CEQqVqITS1n5cFCUIinIXTk6ZID7C78ehqBRNmRlWNly1WCyr4IrGMeB9Ei-KcOX2fCbJ77Bx9ncF6oko6PfNIuPQcPkxbr5lc-s2sjxPAY5kfQTI_15N_YJorQuwl8gtiGi7U5zY7MP_f6rpoFU2Pn9cr9aqXEST2meGhm0szIFrfvNCGpGAwfWTPZ8mw1hOUP3QMIrMkFhWjNM9i_9VhlGZ1qIdvJ4ORdW0LdxTHCzwQr_gimJdzaaN-mY_Hs1qoSYEPEYBw6LnchtjktRMy9U0ezyaugTBt5PW3Zq0m5s1I4GrSdNSZgbf1qz9MiR7x-x-wavo3W5kYS-bOSHH9fI9UQrFjt7Z8zyXM42akV6XI4amB6jx5tdq9LR4mLCoOQiNqwYUzioAKNx0HHTl5WjxDJux3MW6Xjkhz2zIHmkgX8t5FQagwDfrRfajYa58PJvbdIrVbqK1pNEMa6jPV0_-w7OBbApnjfNdafSxcvoJMa5S6uJk9JkNI0EYlHx3OF1kIlMU6TaJ6jGcu8P9YWr7ABpC_9bNLuphEwjX3c8nu9mQYRqrJaJOUCv7sojqKw7SC2ZPZML8OD-m1mlHCHfjYLSeHj7_TS4wk7VCIRHCAb-_BxvCq4aGcH5uXKmAfULrjASsAwsYwHId4lZQn2k2FqjXBq8GTaCkDmyT4ZDPmpTP-iE7IXpnHn4i6X_xpHWSIYDS44zh4RW8OLmc-zBmX58A4ryU2OTTxIcBph3sFPnTWHBDYQoc0aQn1iXE_nu48jz3k9CSkfAt1GpwN9E_up_EH4LpQhyatdtqcxnDGYZjeRV0NSn_mIlji-U3VnEG0zKPg3SRGMNNj43bjXmg0cv5ckThfu3DHu5sIETgiIhurOokIf4zxI2FSdnrk_Wh-ryIHg58ODkN6FdAQEWBfDshriDrK3YS4qaIYofD_ATu7TaLGuWAeUadsnpKGqU4potuwnJOyY6v1u8zgXG3uG9y-fPrP8oJ8lNDhGYW_gw7yQqucQPhgursHl5NSAHS1-JDXTap5OYtp6IyBfM_rAX_INcoESS0pLQDCT9jmdbkN8DefftEUlvAH3FBN4QodF8fY2BUnQ6w-h67uJ-MDpo6cTRR12jWyBg2KgdqCDH9ysuUjXWQnopNxSildkJAFL-goCQVZKheFvwX1aroqW2UFxA8dENm7DtahAjeWacnTqAarmRAOc_GS-g9Kd-EEfjMxXjRDjsBfCyoP8rUzYf1HCfZmu6ZOaN9JkiDaPSia4lnS32vNAWt-xymTeNTmTlbOewhaIgGSOZ20vsMvvUzLTf-Nez4IpnxAFsx4QaUfMxoXsT9pQCKZXnjZJB_yolI51XYv5v3m05OzU03U7P9n4jTcDy3-6sEU2ZUm652Ldu5dGMD8_xmlsKSAW4aIPEyZV2xOWlvjOUAiZ-uUcwM4K9wzm9eA5svg-AjWI40fdabKHYlIxBjHRQs57D4ak0EKHSCLC_swoZN1akiCNDSxYeyiqt1fGZdJ7lfFXW4U5nD9xRV1cTUXXlMljExrlXUzbiE4ChNi3Mv--QjMDaQlK0Z6ngGolvoOORXlCFqwjyQxKYg47Fuj8r3IY3DkN2617JeZN_x2qyRfvopepSQu0H-FZdXiZxwUgrqQVYulKBy5bPCklQ8IeOgqEZO5tfREzqarN-wKvANhFuL3azKbNHv407q19vrx9OfcwDWelodjswrXgMJES_7LJKpNJB2YGvyNUt4inS-h-F-_NWOkhQIUFCFGbsVKvqOBYEEOZyfNcFyScm2f_h5V2IHfTEaS7jTPa1keN8ystIrJ0kUnPhWxNyTzcSKfU3wsOxK_LK86WSAs7b3nigP24jY_y9NQCw7cc0Ru4HkV9R25DmMCARC3sBn23BuJak8JRisNhXjQYF63GsJM-qVMAOefy0IHlcSxVrM-e_plRwfa1bn3gukjh1Dka1-oEIKxrbtnkbRBbhOmoCC91Bzeu_Ivgx4MJrhnJITSDWZ_bmEa4Himd4jrwqj7GsGHH76YEqTW3bV-qQfb80NpY6Ao5tBX3cq8DvHkLmu8IJldEuxPQl3Sz5s8WXloTs0zlUm23IEmgdsR4UP8rGyAQyRQNoBZaPp-G4glM90qamocx3Qv6E9XgAvOCzy4D9Gu6a5WJKGWs35r98snvYZSLOenMeKHLAmTEk5PWSfKSR-kNMLnRWwMH5Odmsj4FwpFmuwDSGyczdCGL4QcgFzo0l4kI_8Cgz8wCd6sk7z7BlC3580sbK46P0PiTSWbswaeRd9xEMW9vTPg1diiTF80JwaXNSeh_9j5BmGKd3bMXBi27nga5ut9fxb8a03gLTkcgdNqPzktYgfU4N4ZjJzCV5WJRbWO8retS0ITd88IVIOjnL0k0bFBKlrbAKjeWr_bzWnPeKXqc5QVPt7xa-Z_visFfsyWqpaIlULnzSgFdshFZ0x02xWkMHfIPpk63IP4WP0E_XN5r8Aw1V6CooXQg46JD-Tj_421rUA5Mt0Uyp0WnbhqdlpcSeBpKyqZkLURzssQRsCSwbDWJ5C-oMwxy6aI03oXfIjuGLi6uKmiR2KjLozg1jYa2tzlGTeF_naok6O69hPByjcNtXORw82qO4AA-2E_UOxJV6X7OpxrdytNoJD6zFCkKtTYtArJHMXwjiQjCq969YgXqE9jHHMRkUDWj6iNFlnxvJm9XYb5nQ7CNstgh4PmJ8jkZf_SUNGU--U-F8ac8A2VzLYUgH6PBnDOYl7eEqeWvgzOhXXxAsmvt2UqKr39xk9thrn_9sTDAwBQC6jh9O0v7ftQunp4UjZbwOQ_5s1ddBuhdS8zoe-X6EztKc2h9aBqxnOSrwTWA5fKpwTTeFo3E0AQLEZLfeNbAcYvfSj2VnkvpG8JNyi4liD97fwUtLmnuhmukoVWq60uByVI7xYmM3vgNEGy5Eg7NPippYXtLw0nK7FwpRMUj9Cas4zo9Cw-y0YwsdMNbThw8rvjTfXSrJ5_70cxB3AOe4P9I7ePjbih9phVW7186Sz2rMxvR741IQV-86tIMxUWI9F5a2H1tm1i7dsLo9ynCKmw6V51omQQycSAZTwgBX1fUDmKNRseoMO0US4FrG6yeZrLIahtXNsj4wKMIYUhS6wtw1Zzd-ilewiDqqC9yMVZLe7pSdLq7zpWoNr0dcekLYXVIXWDz2pkX_tEKQePq6QL0juRSP8XNBlGhiZzennYJxo-DR1mCGjciWFqahy6wxPK0SYK488YJ8dmu5WzP8I1mfjgtAw1GliSOej3rY6_u_aBG82VgiXxQUH2p0fPz3nnYe7lxMW8_vpcqyNqSVmeilgi1N8wjaMB2ssmDAE7rR3jT2nfvVXhDqrPIXNPh6u1EKT62K8wkctqeKewJwNAVJS_m3j2UmlhDiRoPGW0vFRv9h30OoLj3BXYtZ7iwP2daF7rf2fL-TesKM3uqwBCbQ_FFGe7wu810SLohXWcEDoGa6G6jNx9F-_CYVZnMpzwTGvnc652039BEsaCXWxSEr4Yg4VMYsi8U4_1YSNaXBHlMx3IcPtMP3S83x2xVXx8I5gfrNUCY-k0Vj6YCcSPQRXPS_eLNoTIHdbl0Jl52nZpk0UGq7DukuJWTg1qivok0wEDnHMO5nBRtosZhc7FBVtR6NrZryZ4RUcABxTUeasJNY8BwvhfVxyWAeEsGeqnO5BAF4PvMob4aIh_az8a0p8uVGXn3NyZOK7sqCXVOgvhiPVxOHugeVeKX0Px9T85ewcuKxTWPmDdMitjpbONbwv6xZ0aE8Zm1_3KFpjh13fdu_PrUGaqCjZOMZ156AaZek5dzgUmsR1pRQWbNMhQYXmzhwqgqxP2zcZI9zNfFVWQ5orUkPJ25YHIPDI3pWPHomXHV7wBLtlI9MKhZ7lKW528K26t4we7ewo5Dj8x4htvKLIzkRepgCsoYXXPJG8ISn_G4X02H9Cg_82rlkgthVeneUyx3Dp-d19PdBNQeVJFt_d2kCewnvDqHrLAN5_DIWEf-qkigqHs-m7GY7CaAzxFlv8YEBFeHsE0EkLmDvXmFKrytrDu9gU5yuEGo7XxYpmDJDtHjmJkOhrdVLoUX3QwtTOjgJpWhsO47DZfMowiVMa5jmv7S55XvrRFoIZFlBCF75Opc49lzYyWaEFTmh4ftxY6cdt63aY9uKKbPJv_Su0wyoeqD-fLVn83MZs-Fw0chc7HqfFJCikaLwe1M0nxo8wqMIcfhNMYTZeoz6dSHtrwvxw%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5C%22futura_exp_og_so_72776762_e%5C%22%5D%5D%2C%5B%5C%22%3CHtJq0ooCAAbV1vff9daN6IX1Fmilur_0ADQBEArZ1JW_Bzhtkn_WqleJ_cL80Z-ocP5sTDowp2Xen-18mGPAqD4ffVrkQ_t9mkz7KraPzQAAAj6dAAAAIqcBB7EATbzTbvA3cPQkojybX5bViKQROnFcfdDhrhl-jmmWphs7JMeslHuIV50hPhrghyLTAbCUjDodpfNO-jq6dqdszmHqA1JVU-svBEyEWeBQVg9VqwDhZI07j98LD9fcej2btqNmVKiC9BhP_vR1HPd_zUtQJGdDrlkd8TzAZx3AZvPhmnyag2QDUZfc6YK7Ta-eoRx9_ixOdwjgnd17L2TMNQLqxBMI8ChxxJVT3-YbPjY0CkyofH1l1UsGhWuVxAh0rMyZ97t-kz69CtE9rAuUwwBVaMQIWF5QX1A9Gpv3RyC2dz2LEJGP6fIolu4ZAU0amwdi5lvbduq8mQHaKYMxNtftOl4mP9rfFYAs1TgoqJ649VllWLYPkRfBHCFSqvCShZsiRN-dme9q7NCgcIoO8ixnPWL18FNEcSX-kP9zNM0QF-aTxCGykF7DMISIFD3N5-PwdNaKklLiIEe7JNgM4Ti3bl5s17vyY8wDNxmdXRnYDoeoLMQbi4By9jBhRS8_UvcaNaonXcuk_kZ4zTwY8H3d9Tjkn4fuXcaiH9FEoybOcbk08l1b-rcPx31Umw2yWoB4xmXBVE1OtRWoP2soa9TF4D3DKin0nYLHcWaumIoH-TI8q5UKnSxXA6XrdsEJPyrgxC0TcARC5gGcsg1LjxcnqZWu2K59-aJO8unc1lP2SDKluTPA1dz9bOe9upZrpCgFm9jiba9Pk0q40U1oF-z1a6oNYysfECfEEvtVSndHWWasFH04ETSXsN62fZC-NW5AFqEpg2_z772G0tspGEw3e_935eijy5pEk-9rwzF_eWgS2_QJ7xNjwrGFy3_GkafjDyzO8Dx_xdLK4WIY707VLtmMc93Dx6ko9bVWZmEVz3KYRuMMt__wJce7_16RM4taLQp_iD1cCh4ROimmwzVu3_wIS9AayI9SABnJS0vSse2jE5SleN5Uw4FvaijD-_p01imq887t4_jnpvKLzsQvv4tFYhY0LvP32Y3xLgEh6DI25aDXXgMEnMg0AOxxlAyviNAPFdB4bu-O3rU_egPPhrojfscB9a6G3VtYXt0El6CyBKZ3_aos3CEQqVqITS1n5cFCUIinIXTk6ZID7C78ehqBRNmRlWNly1WCyr4IrGMeB9Ei-KcOX2fCbJ77Bx9ncF6oko6PfNIuPQcPkxbr5lc-s2sjxPAY5kfQTI_15N_YJorQuwl8gtiGi7U5zY7MP_f6rpoFU2Pn9cr9aqXEST2meGhm0szIFrfvNCGpGAwfWTPZ8mw1hOUP3QMIrMkFhWjNM9i_9VhlGZ1qIdvJ4ORdW0LdxTHCzwQr_gimJdzaaN-mY_Hs1qoSYEPEYBw6LnchtjktRMy9U0ezyaugTBt5PW3Zq0m5s1I4GrSdNSZgbf1qz9MiR7x-x-wavo3W5kYS-bOSHH9fI9UQrFjt7Z8zyXM42akV6XI4amB6jx5tdq9LR4mLCoOQiNqwYUzioAKNx0HHTl5WjxDJux3MW6Xjkhz2zIHmkgX8t5FQagwDfrRfajYa58PJvbdIrVbqK1pNEMa6jPV0_-w7OBbApnjfNdafSxcvoJMa5S6uJk9JkNI0EYlHx3OF1kIlMU6TaJ6jGcu8P9YWr7ABpC_9bNLuphEwjX3c8nu9mQYRqrJaJOUCv7sojqKw7SC2ZPZML8OD-m1mlHCHfjYLSeHj7_TS4wk7VCIRHCAb-_BxvCq4aGcH5uXKmAfULrjASsAwsYwHId4lZQn2k2FqjXBq8GTaCkDmyT4ZDPmpTP-iE7IXpnHn4i6X_xpHWSIYDS44zh4RW8OLmc-zBmX58A4ryU2OTTxIcBph3sFPnTWHBDYQoc0aQn1iXE_nu48jz3k9CSkfAt1GpwN9E_up_EH4LpQhyatdtqcxnDGYZjeRV0NSn_mIlji-U3VnEG0zKPg3SRGMNNj43bjXmg0cv5ckThfu3DHu5sIETgiIhurOokIf4zxI2FSdnrk_Wh-ryIHg58ODkN6FdAQEWBfDshriDrK3YS4qaIYofD_ATu7TaLGuWAeUadsnpKGqU4potuwnJOyY6v1u8zgXG3uG9y-fPrP8oJ8lNDhGYW_gw7yQqucQPhgursHl5NSAHS1-JDXTap5OYtp6IyBfM_rAX_INcoESS0pLQDCT9jmdbkN8DefftEUlvAH3FBN4QodF8fY2BUnQ6w-h67uJ-MDpo6cTRR12jWyBg2KgdqCDH9ysuUjXWQnopNxSildkJAFL-goCQVZKheFvwX1aroqW2UFxA8dENm7DtahAjeWacnTqAarmRAOc_GS-g9Kd-EEfjMxXjRDjsBfCyoP8rUzYf1HCfZmu6ZOaN9JkiDaPSia4lnS32vNAWt-xymTeNTmTlbOewhaIgGSOZ20vsMvvUzLTf-Nez4IpnxAFsx4QaUfMxoXsT9pQCKZXnjZJB_yolI51XYv5v3m05OzU03U7P9n4jTcDy3-6sEU2ZUm652Ldu5dGMD8_xmlsKSAW4aIPEyZV2xOWlvjOUAiZ-uUcwM4K9wzm9eA5svg-AjWI40fdabKHYlIxBjHRQs57D4ak0EKHSCLC_swoZN1akiCNDSxYeyiqt1fGZdJ7lfFXW4U5nD9xRV1cTUXXlMljExrlXUzbiE4ChNi3Mv--QjMDaQlK0Z6ngGolvoOORXlCFqwjyQxKYg47Fuj8r3IY3DkN2617JeZN_x2qyRfvopepSQu0H-FZdXiZxwUgrqQVYulKBy5bPCklQ8IeOgqEZO5tfREzqarN-wKvANhFuL3azKbNHv407q19vrx9OfcwDWelodjswrXgMJES_7LJKpNJB2YGvyNUt4inS-h-F-_NWOkhQIUFCFGbsVKvqOBYEEOZyfNcFyScm2f_h5V2IHfTEaS7jTPa1keN8ystIrJ0kUnPhWxNyTzcSKfU3wsOxK_LK86WSAs7b3nigP24jY_y9NQCw7cc0Ru4HkV9R25DmMCARC3sBn23BuJak8JRisNhXjQYF63GsJM-qVMAOefy0IHlcSxVrM-e_plRwfa1bn3gukjh1Dka1-oEIKxrbtnkbRBbhOmoCC91Bzeu_Ivgx4MJrhnJITSDWZ_bmEa4Himd4jrwqj7GsGHH76YEqTW3bV-qQfb80NpY6Ao5tBX3cq8DvHkLmu8IJldEuxPQl3Sz5s8WXloTs0zlUm23IEmgdsR4UP8rGyAQyRQNoBZaPp-G4glM90qamocx3Qv6E9XgAvOCzy4D9Gu6a5WJKGWs35r98snvYZSLOenMeKHLAmTEk5PWSfKSR-kNMLnRWwMH5Odmsj4FwpFmuwDSGyczdCGL4QcgFzo0l4kI_8Cgz8wCd6sk7z7BlC3580sbK46P0PiTSWbswaeRd9xEMW9vTPg1diiTF80JwaXNSeh_9j5BmGKd3bMXBi27nga5ut9fxb8a03gLTkcgdNqPzktYgfU4N4ZjJzCV5WJRbWO8retS0ITd88IVIOjnL0k0bFBKlrbAKjeWr_bzWnPeKXqc5QVPt7xa-Z_visFfsyWqpaIlULnzSgFdshFZ0x02xWkMHfIPpk63IP4WP0E_XN5r8Aw1V6CooXQg46JD-Tj_421rUA5Mt0Uyp0WnbhqdlpcSeBpKyqZkLURzssQRsCSwbDWJ5C-oMwxy6aI03oXfIjuGLi6uKmiR2KjLozg1jYa2tzlGTeF_naok6O69hPByjcNtXORw82qO4AA-2E_UOxJV6X7OpxrdytNoJD6zFCkKtTYtArJHMXwjiQjCq969YgXqE9jHHMRkUDWj6iNFlnxvJm9XYb5nQ7CNstgh4PmJ8jkZf_SUNGU--U-F8ac8A2VzLYUgH6PBnDOYl7eEqeWvgzOhXXxAsmvt2UqKr39xk9thrn_9sTDAwBQC6jh9O0v7ftQunp4UjZbwOQ_5s1ddBuhdS8zoe-X6EztKc2h9aBqxnOSrwTWA5fKpwTTeFo3E0AQLEZLfeNbAcYvfSj2VnkvpG8JNyi4liD97fwUtLmnuhmukoVWq60uByVI7xYmM3vgNEGy5Eg7NPippYXtLw0nK7FwpRMUj9Cas4zo9Cw-y0YwsdMNbThw8rvjTfXSrJ5_70cxB3AOe4P9I7ePjbih9phVW7186Sz2rMxvR741IQV-86tIMxUWI9F5a2H1tm1i7dsLo9ynCKmw6V51omQQycSAZTwgBX1fUDmKNRseoMO0US4FrG6yeZrLIahtXNsj4wKMIYUhS6wtw1Zzd-ilewiDqqC9yMVZLe7pSdLq7zpWoNr0dcekLYXVIXWDz2pkX_tEKQePq6QL0juRSP8XNBlGhiZzennYJxo-DR1mCGjciWFqahy6wxPK0SYK488YJ8dmu5WzP8I1mfjgtAw1GliSOej3rY6_u_aBG82VgiXxQUH2p0fPz3nnYe7lxMW8_vpcqyNqSVmeilgi1N8wjaMB2ssmDAE7rR3jT2nfvVXhDqrPIXNPh6u1EKT62K8wkctqeKewJwNAVJS_m3j2UmlhDiRoPGW0vFRv9h30OoLj3BXYtZ7iwP2daF7rf2fL-TesKM3uqwBCbQ_FFGe7wu810SLohXWcEDoGa6G6jNx9F-_CYVZnMpzwTGvnc652039BEsaCXWxSEr4Yg4VMYsi8U4_1YSNaXBHlMx3IcPtMP3S83x2xVXx8I5gfrNUCY-k0Vj6YCcSPQRXPS_eLNoTIHdbl0Jl52nZpk0UGq7DukuJWTg1qivok0wEDnHMO5nBRtosZhc7FBVtR6NrZryZ4RUcABxTUeasJNY8BwvhfVxyWAeEsGeqnO5BAF4PvMob4aIh_az8a0p8uVGXn3NyZOK7sqCXVOgvhiPVxOHugeVeKX0Px9T85ewcuKxTWPmDdMitjpbONbwv6xZ0aE8Zm1_3KFpjh13fdu_PrUGaqCjZOMZ156AaZek5dzgUmsR1pRQWbNMhQYXmzhwqgqxP2zcZI9zNfFVWQ5orUkPJ25YHIPDI3pWPHomXHV7wBLtlI9MKhZ7lKW528K26t4we7ewo5Dj8x4htvKLIzkRepgCsoYXXPJG8ISn_G4X02H9Cg_82rlkgthVeneUyx3Dp-d19PdBNQeVJFt_d2kCewnvDqHrLAN5_DIWEf-qkigqHs-m7GY7CaAzxFlv8YEBFeHsE0EkLmDvXmFKrytrDu9gU5yuEGo7XxYpmDJDtHjmJkOhrdVLoUX3QwtTOjgJpWhsO47DZfMowiVMa5jmv7S55XvrRFoIZFlBCF75Opc49lzYyWaEFTmh4ftxY6cdt63aY9uKKbPJv_Su0wyoeqD-fLVn83MZs-Fw0chc7HqfFJCikaLwe1M0nxo8wqMIcfhNMYTZeoz6dSHtrwvxw%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5C%2203AFcWeA7RpssgraL6HIPsNF3grIH4q_x3TBp3bMnWYfLMcm1k_3a0xIfg2iFVXpFmca-ENGJj3Wngoks1Gkfw1cQC4_VkmUc_rVq7-OZFubDsY9XeRGcKHY_0ybVTL9slCPcWkSuocoJ1Ye6tXQIFyrcY9sp5NYrTlZGlFaSrzz3prPgrScOjXnQFP009Fye2TsxeW806MjQ5mK8dGlAqGer8q17BZqwy0uJeKkStSGcc14UOkn6wVQDQtrFv_lfswGS9bPeJfGGbTRiEplsqeDuYEYKMXtolR2kug8Eq0c0fjW5areSx3EoY3_Mc3P-jfSa5VJ5IfHzPJWf5FWcYM1fT12EbxnwxgFRCAI3jVs9JMK08JLM-Bru3TuHCDo-Tm_2UZovto-1iPYuON1d1RYlUPCtHoj5WlKIMkTQYoFIG5JTHpq_Ph0zdTAKDMpFwuSgPUp_cN_-WzoInkvh5TL9lr1YK6f-pHF1h9C6ddxUF9s5e_rhKSx922C102i8yFtPR6XWE9e-FTF1DzjtFbXJ0vY2FLHxoEpE5OwQ0z1QomJr15_mCYmnzkNr-Qh3yDmixUM6gDhA9Hytps-JVvjdITIv-ATMlSUEdKu0_js4kUtyYV8PcpL4DU9OmELkaYdrFFn-Km_66mzJWYnrpENlTL3KU2P7qdFvAWjUJU79sdA9yZnvUNQ2fZfD6o9Xq-ADZIOwC73puHwIlHZCX9L3BW_6AP4qB-8nYrA7MzH7m4eUGubI_QCv-nGA__9M-oC_KUDdZTwpU0PHKFUXHbxPn0eTdCPCl_lOY3N55oHB5lAARxcmLJSTYGsJV7bNyhGHRee5Y_HqE_ap5VXTB5upu88J5w-1bPhhBzoIgpiGOiQ6tIHlVDhaemfBniM-1VvQqHTVYKo5alaOmnxdpUJ3Yym8tlM1h6xdFd16EAplizb5VCAbFsOmcRkM2FE5f0Z5nx-Pvr1aldvGOW5BcbZBkiWkb3pSfA5nwMB9Q2pa9NVUCwKDP8QQx0MbcEJvJN4yig9MoRJ_7XXVAp1jrYCzTt7D9GqD_VRvgB5m3A7VpjellJolJkxU0lzPZaFL0ZXSpVpJE1BeIwwtBBRdVnLN7JHbsf5PXU2PJ9-3Cxo70Zm61kH4cda05jPaTASI6gUwZlhYsRioqrcBg-xt5aPJwFHJuQVQBfdpFM0hApZIlr6yYT39zKrWfxklCfulF083fwcCuYZKcK0kt_peR4QaJnhhb1zZWR-sDTxWeXL_1_nSK2h1QfEpRfxd3iQQMTse6JQ_FYfXgICX0VN3N1E2cJ8MxINnL1bMvBti6vqBAT0tsjjfmX91qVnxPmlAHl4-IWp1aQQcqh-xRQ1KGGlFvjiL-9mq4n-gHSrG1HUeMudzR_w6jXqqRFpdY7cEPh_33r8fpAMSFVJqUMdq9nq0NPPUelC5VuM238O2uOL2alt3L4Y-dcjsQ5pEwNVUDFXQ6sbciS9PE8cvagS3AZ5fVm5zLsdEkDNu0bs3cLnwI8AIBsazWzExu9z9kkMkiJMaqBkHnsfsPyBtLbDlAH8W-cJae0PPW6gLYlwu2tG8PWW6z9FGzpT_6FKO9dBkYpZg4CzFwP60EmuGOiISjxte63njdGGqGvtAglr1pvYFq6jF7emJ-ozejTQCqLwLotf3Ocl0OXbuS-ZFS4gN4fZbHwVRfg1vwDJbjQt-V5suIFyhJUuD6ACGgbv9lrxvsfn-p8hqJM08oGDkxU32FKwYCLVV9kCpjIQ1X2Xu25QKJFM-pbzL8l-x9p_x1yqna5wcMVuNfSw5EWMmAlikpq2QDUASRmeZ39xSDc2SKW4PQ-C1qKOjYwQDma2B4cZHdy9frUeuXqTurgAXeB-yJrkpNt7J1CGYKFUGlZTaybdn5MWDF3P_4Uujlq4q0VYTqNXJRAUw9WpfiJ2kE3M3kNdswIxfZqexYfuQDEXF5eOF1FBfiRYWVSHGTC0-_tzqi9rGU8BuAeqwHmElvHZWwnk02jApyr3zTzcXyTHckMqAtWAmkduC3-rgzp4sK6umlemvBnQG_ZibZ%5C%22%2C1%5D%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(
                random.randint(1995, 2007), random.randint(1, 12), random.randint(1, 28), at)

            response = self.client.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,

                headers=headers,
                data=data,
            )


            headers = {
                'accept': '*/*',
                'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://accounts.google.com',
                'priority': 'u=1, i',
                'referer': 'https://accounts.google.com/',

                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',

                'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
                'x-same-domain': '1',

            }

            params = {
                'rpcids': 'NHJMOd',
                'source-path': '/lifecycle/steps/signup/username',

                'hl': 'en',
                'TL': tl,

            }

            data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C4772%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(
                self.email, at)

            response = self.client.post(
                'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                params=params,

                headers=headers,
                data=data,
            )
            if "password" in response.text:
                return {"data":{"message":"success","status":200},"message":"success"}
            else:
                return {"data":{"message":"email is used","status":302},"message":"error"}
        except:
            return {"data":{"message":"tokens get error","status":200},"message":"error"}
# print(GmailChecker("atroNteo1231q@gmail.com").__str__())