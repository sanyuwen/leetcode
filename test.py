if __name__ == '__main__':
    a = [
        {
            "statusName": "PendingSchedule",
            "statusId": 0
        },
        {
            "statusName": "PendingVendorAcceptance",
            "statusId": 2
        },
        {
            "statusName": "Scheduled",
            "statusId": 3
        },
        {
            "statusName": "PendingVendorQuote",
            "statusId": 5
        },
        {
            "statusName": "VendorQuoteSubmitted",
            "statusId": 6
        },
        {
            "statusName": "ReturnTripNeeded",
            "statusId": 10
        },
        {
            "statusName": "Rescheduled",
            "statusId": 31
        }
    ]
    d = ",".join(r["statusName"]+":"+str(r["statusId"]) for r in a)
    print(d)