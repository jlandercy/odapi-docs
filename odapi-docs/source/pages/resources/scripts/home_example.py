from odapi.connectors import Irceline

client = Irceline()
meta = client.select(sitekey='41', measurekey=['NO'])
recs = client.get_records(meta)
