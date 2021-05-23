import mail
import InvestTrust as IT


def main():
    dest_addrs = [
        "yyyyyyyy@gmail.com",
    ]

    load_urls = [
        "https://www.bloomberg.co.jp/quote/NYFANG:IND",
        "https://www.bloomberg.co.jp/quote/QQQ:US",
    ]

    subject = "My Daily Information"
    subject_star = ""

    message = ""

    message += "\n[InvestTrust Information]\n"
    for load_url in load_urls:
        data = IT.get_data(load_url)
        msg  = IT.data_2_str(data)
        if "* buy" in msg:
            subject_star = " [ buy ]"
        if "@ sell" in msg:
            subject_star = " [ sell ]"
        if "*** buy" in msg:
            subject_star = " [[[ buy !!! ]]]"
        if "@@@ sell" in msg:
            subject_star = " [[[ sell !!! ]]]"
        message += msg + "\n"

    for dest_addr in dest_addrs:
        mail.send_mail( dest_addr, subject + subject_star, message )

if __name__ == "__main__":
    main()
