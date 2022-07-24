client = Client(account_sid, auth_token)
message = client.messages \
    .create(
        body= "Check your phone.",
        from_ = "+15164004128",
        to = "+9779806736272",
    )
print(message.status)
