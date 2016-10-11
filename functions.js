

Math.round

msg.payload = {'d' : 
                   {"temperature" : Math.round(Number(msg.payload.temperature)), 
                    "humidity": Math.round(Number(msg.payload.humidity))
                }}
return msg;