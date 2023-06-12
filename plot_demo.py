import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Data Manipulation and Visualization", layout="wide")
st.title("Data Manipulation and Visualization")
st.markdown("""List numerote :
1. elem1
---
2. > citation
---
3. ![meteorite](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgWFhYZGBgaHB4eGhwcHB4hJBoaHiEeHCEcHx4cIS4lHB4rHxkeJzgnKy8xNTU1HCQ7QDs0Py40NTEBDAwMEA8QHBISGjQhISE0NDQ0NDQ0NDE0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDE0NDQxNDQxNDQ0NP/AABEIALcBEwMBIgACEQEDEQH/xAAcAAADAQADAQEAAAAAAAAAAAAAAQIDBAUGBwj/xAA2EAABAwIDBgUFAAIBBAMAAAABAAIRITFBUfADEmFxgZEEBaGxwQYi0eHxMkITFCNSYnKC4v/EABgBAAMBAQAAAAAAAAAAAAAAAAABAgME/8QAIxEBAQEBAAMBAQABBQEAAAAAAAECEQMhMRJBIhMyQlFhBP/aAAwDAQACEQMRAD8A+WNc2HSHEx9pBAgyKuBBlsSIEVIM4HLeTe4EAboBEya1k4yYpakKAtbUwzRPerPuoATSJbgQaiLGIijgHA8iCCOBClpQ4AEwZE0MRIziTB6lAogKGJtlzm3KJ9FyvAeOcy1r9eC4SdvXXqUtSanKrOrm9j0DNu14pQ5FcHxHh5NL5H4XAY6DTv8AF13nlgbtKO9brKeO5vcuj/Vm5zUdM/YlpAc058/RZOaQYIINjIghezf4Vm7uu+4YHEfpdV4nyrBgJWst/rLWJ9z8dAHZa4dvdC5+08reBMQuI7YuEiMdaCbPjIxGtf1aEl1ScKca8Tz/AAsyCEwenSfdHSUCYOOOu6twEkTMWrEjA1Fb2WbTYG065JlvLvrkn0LPaaxhbiVoxuVTSkcK1Fb5JWPbXCioKpU1u/abzw+N50yQ77t4zP3EAbwMRHNYl2E3g8yKCa8THPiUQYOVAY7/ABKll6x+OyfS42Zt91r2YOiRxaQRhOESINcpBykxaf0PgFXuXLiZuMSTQ36ntCw36bvuaTWD6nulbRE7XaTWAL255CwUNzJNqRjhBM0pOeFIMpvNhqqqJpQnPnSpOFPVQtJbTIGYJm4FqcaWxHNVs3Va0kAFzZO4HEC05mn+tio3aUjUZ6ugtm1OZ526RnnjAAybadTX8IWhEiSRTObAGBPSAPYLMJKXKUoFaRPAXVveSZmTStsABTkE+hNUpVDGBOdNYpE0j5+Ewrf5IUbyE/1Q0Jpy1bv3UBa7QkmSAJMwBAAMEQMslHTrlw1kpChsxul01BAjgQ4zef8AXL3CTmxINxyOWIOXP8Nv2niK1jmKGhHupn3w/AQkiiE1bGgzLt2AYoTJuG0tJJvRIM51r2VNMVAnmJzSLY6j55cMEEVuMM9SgAPgzlWoB9CIPZb7Hb7hIaaTQ55GCffNcYhaMJPLkMsOMdTRXkO68L4yf8jqma9N5SGOAEiSL8cp1deCY+IjhwjjS3Ndp4HxhDm1IECZOv4urPjmoedWV6rxnhSwy5tCRTMZ5EfldJ47wYJ+0QBhHovd/Tfjtk9n/Htvuyn/AF4A3C4vmflTWSdnNyan0IXPvx8vI6JZY+aeK8IWn2jWoXDazvFLXnH1ryXtfGeC3hvAfdi0rqB5aTMt3SbCL8vwokRrxWOjgAkiwFN6sgmAaxJgg2wmIUtYT8ccKZrk+J8OW2Gv4sf+MjCvwbUT5WNnDDet665LVjxMmtOVYgHpIPGFLBTXshxik0+E4ihxgiDMjjS470nqFoQT9wLZn/UACSZsBugegAApZZOeaQLxFLxIEE3FIj/14JseAK8hwrPXFEo4raNMA5/v8Ljk2Paa8MdUVbRyl5pYCtxmOsYi2fJTb1UiXG3D1/KbnQOPwcPX1KgtTg9cKKTIDj1+c0jUxQX1wyQ1xEjMQeQIPSoCHNrcaqhSSM8sfhauO8XOJuZriSampvjf0sm1DiSBEG1ThA7inLJICLxPccbXHI/lAJkzImmIw48P2hw5WFuQyxrXHOqKyYFzYSb2GskpCA1ZtnNA3XOEGRBIhxoTQ3gRKgbQ7pbg4gmgmkxW4ubXxTDhuuEVJFaUAkxaZJioIoDQzSCUwW8mkhINd2daopCAqIjWuCaSBqJ7T8qzX4BJJ4AUwAA7dJn19EgUgZfIAOHteOUyepQXE61oqogA0Mg42qRgaGkgHhQg1TGyYxJAQERj88Y7ojAH9ohDa0ry4oAc6v51qiCcUgK6+VZNIAvmAcTaktw51TzAvZPAkRMiJOFQaXg2r/Do3amd6J4VNoESaxHwsDbrbOlDzurc2k8oqONYvH2nlThPVjVz9Ku58u82LMTw1rFe28r8/a4BrwCHYz0HqvmG/QZA2te9RU26LkbHxJFnECmMd8Ist+539POrl9ZHhWPlzY3Zkc6jnSPZS3y5m0AYYY//AFJ/xN6E/wCq8n5N9Tlga2BINTmONYBXtvLfFbPbQWn7sRTQWHk8P/Ljpx5f59jz/jPpDbMLt9lcxZw6Y8V5rzDywDCDkeM21ivsXivEvcwbMWGd6ZLqfH+SbPasBIh4mDgQcCufPl/N5qel3xfrPZ9fHNt4Usw1r2WDh0+V77xnlJILY+4UiLrzPjfL3N/158DHHInrC3vjmp3Li1m5vuOmbs4EkGop+fRDyDEZ1wFYprNVtXm09ecdVlvQIFzrXRY6nPQkRtRr4UEcMvWs+q1LTckYiJqMKgVCnd7ayWXVyE4XqPg8RCTWnvnwx91b6ySf2nSKisU749EdP8s2tNYmBU0kADExSJMTaqzAWvCNdUBtJ1h+UdHGJKb8bU51sKTjWe60NDNOSmoORv3qPQo6OIIiQU98iYJrQxiMuIoFrEAyARSaAwLiHQd2YNsktj4d7w4tEhrS51qNFzVMkGhgwQDcY8jFqZJEnKBe2cYmpFM1MKi6QBAoIoL1JrmaxyAQC3+A7JpbyEBZCpwMAwYtPEVj19Uim18AiBWJMVgGaHCsdsplpKUwNcq9qeiAyk8+4j8pxy1KQTKCddEJluVc+H6sgJ98EjecVpA521rJRw0UAjw7aOpTGWscVMpwiBYNCaf3ILQEHGuZm0AD0HYBYjWtXTIy5QO2NVpPJRYtwgRTCuMe1ZFq07jHxHL0qPVSya0kXJiYEj5IHUJk11XvyV53PsJux9pwPUA/GPXiu48k82ds3NM8InCJr64froiLkSLdjNznb1Vsd3trt6rqx5e/46L57j7T9PebDbD7q5xccl6J/hq0MjiIkcsCvifknmztg+piONJ0LL6x5B54Nq0WOrLn8/i57/jp8fkv8+u023lzHitxn8rpfNPpxjh9ol0W1ivW7ItdUGoWo2YcLVXJN6x8+NLc6+vhfnf0y5hJ3d0zMYHrn+V5rbeFLKOBvJX6H818o/5WbpEkHvReB80+m5MGBE3BjuF0Tc3P/WWs+/T5e7Z4pjZ0tPHK5XsvH/SO2Z9w2Tt24c37gR/8m26rze28CQYIPGk0xPRYanPis5rgDZkdROBkVGuSkD2Pdcksy686/CQ2ayums8bjDlNIuaduKhzdei5h2d66+FI2eECcMOs5Uxz5omiuHGrmRNxh1zuVO9FDUC4JMGMDBBjlC5DmAXzrBHD91qsSO6qaZ3DGEt1aFG0gk7ogYCZMcTic/YWVSouWQAxoEbpMRiaCcevuqKSpIQlCEyUUwK5qi2IoYPrF0idf1JJsbJAoJIFSAMqk0A4lDTr9G/VMOpYTMzjj6V9ki3XrKAmOCcYa6cETlrNMjCmNeMaGXqgJhHpimfx7e6USc5p+kAptzPan7S1zVNArypTH+evVG7Jpwtnah+UAb1hEETJk1ynlwSHJUwXtY31eiTRcSNRalP0gEAhOaz6c8PVMU5+yAbZjhr8q2V4WUN6U7n+LQmTwsKC0RWkTGOdVpnVhVsxpFYovT/SXmDmbVsk7jiGvi7RYPA4GvLmvN+H2oFDjjHCK1giYwlczYbdjrHcIzsajsanoF1Y8kueVMtzqWPsTPGv2W1Oz2v2uFWuEw9uDhwK9D4PxkmCRPBfJPEfU+12rNkzaR/243Xi5FhJwpdej8h89aSK6yXPrx3neOzNzqer7fT2VC4vmPl4fXFY+WeLDmTOS7TZvBXLzl9IvY6HwPgn7LeLXEA/6mo5xgvG/U/0y9737QRJqQB3X1F2zBWG38KCCjvvqpt+fPGeUOYbLhf8ATL7ztfItk+Q9oIjkRyPwvIed/SAbLmWwCw8l5fToxuX1XzB3humuCyOyPX3whek8T5cWmCF1niPCkGFnnTa5dM9iycL3tSvXsuy2myoVxNqzDlenytc6Zay4Tlnu91yDTjcQRmInnWnELItWsrn1Ge7M0k3pwkmgwAHSFmL1tiLU54LXaN5dI+FJbSYMTdaRnUIT1ZCaWorQcT2H4UoCbAZaREzTnSJmmKaCMp564pDsqAEG00x9LxjPRIJVFhA9aEcqxY8DWozCTjW8/j4SB/aAUIJ1x18KnN/nS6mtkANvNu8D3MJW/P4Tj9ItBB/UdEAy2k8TX361HdINvr+pgAcZCHGUADMqg06IylDAIMzwt60VBMqtjZwFBwE9zU1nHK1kS0YTXGk84tquKZ6616JOcJki82pWvpJ7BVSjXZQYpNIwpkT3xvHCl+JYKQMSCZoTQ0yuK2WOz25bJEVHQ1EyJtfVVttMqWEkGQLXjHDhZPvpUns/DeIewiDTI/u69H5V45jiK7judF5ncIAkRMkccPcLRhhKeTWVzMvt9n8i8wIEH7sivWeG8UIBBPEH8r4X5R54/ZEfdvNpT1X1j6d852e3YKw7IrPWp3rXmrPb2Gx2wcFqup2ILSMl2TNoDZR2M+B+zBXF23h5kGoXMlcPxm/H2ug8gp1maOa/LzvnHkzHMMCvyvA+ZeWGCYsvc/8AXbRjyHDfYYkE1DuByJwwnBaPYzb7Pea2hoRi05FcHmzrOnf4PLLnlfH/ABOzIFb95NF1b2Er1n1N4XccQvNHrqVt49fqdVuccF7IExPI5yMuGpWDGF32tEuJpVbvaJIPHvFL4TFVxtpGGFLQSKmTcT1yXTly6YuWblq9xNzagrYD4UHExQLSMKiUIlCom0xPbGYOXSnVIHWaUJg6PI67JsxRAKdAaiRbLrwzSBpFNcUAxXC3rc/B4JDNBAmhJE5VjOJ+UPvFvTNADm++jkgpvNfe18YAAAGQwSKAQokqOuSCOyAQCE28+aoM7d8NfuEcHQGUn0rkD8rRtIpq3XHQUvaadxy1KAaWOUza9OEiac04TU7omoNBncjCLkT6Ljn51rmrbFQOF4/C32GymXWAofgZyS2/wq+l8Zhs6jKPb2VME8IrbWfsuRtRJj/xJielKATa/LILjkJWcVL0OZBwOcHph7ii2jDhjPpOOMfxYsitY+T3gJsFPX2WemuHJ2dCu58q8eWOBBI1wXRCRXP9hcjZvqMFjr06cPuH0z58Nu0McfuC9I126br4N5N5o7ZPDmEiOK+s+T/UrNqwB32uxg0Kxm5m8t4evDb7zOu32/i3scTdmeRTPjw4X/S6vxjw9rmNeGkxE85XmNv5g/ZvOye0h9OoJgOBxbJFVpPJm/K59ePUr03jGNLhiTNPbEc+i08G0t2jgRBc37h/7DdM+pXR+B39o4PJALc67xBMbuGA7813HmHjRsNiXvI/5HC2Q5YUAXJ59frXr+Onx4/M5/2+efXO1/7pC8XtXrt/OvGHaPc9xqV0j3TxWnhnMyNvJfbHakc9cVx3LXaHOnPK4PKIWDiurMcuqglPYbZzHNeww5pBaYBgjGCCChm1LHBzaEWkA8LOEHsoc8kk5mtBjwFBfBaxhUQEJbpTTS11/UEX1jfWaYx6p71BBtwzmROrnq0FhKosNTEfmk8rpNMCegt1vY1FUt1AKRFq611TNseKHmYngJ5U9vZEZxaeaAQ7ob0wv+Ld8kpVgRle2rjkgExonHjnFLZmqI/h98v6raRlQjPHA988DyQTJkkkkySbziSTdMBnKet8e1u2CYkCM/7rkmy38/qrdxpPPL++6aUmddlLc/5K0e4DjaTjjzinNRU2mJAFZ4Adhlgg2jKmvKekDXBc3YkFpbiYmlAMeO9SO/JZMbAkY1rkINTjUcLhaNaYJsL+/pVXn0iltGxha4qIwvzXFf8AoT71wmeS1e++ongOKxc851EVyU6qswF4gYcuZMnjWOlkmuy1qVmXa4WQ1yyrbLeYMgxyw1C0a+tFxw42+Of5VNfXL1Weo2zXO2b4rhz+F2ngPMiwitOf4XQh1Vo16x3iX66sbufj6V5V9TMpvFd83z7ZO3S7cO7/AIlzWkjlIovj7NuRbR0D2VHxjs1y3/5/fZeNP3nX+6dfVPMvrRjf8TJFpsOQFF4fzTz5+2dLySDxXnn7Ym5nrl/FD9oTGCvHgmff2ld5k/xnGm12hoTj6iSPcELjF+Mwc8R+FJfb2z5mVi8rpzlz60HH5w1is3Ow/NUEqHLXMYapPdPp6CPhItO7MQLTgSMOJAcKDCvFJ6kK4ytKULVu7/5uH/1//SE+Et8YfzhrNKeGstZITIpPTHvVNIc1Iu4a+FW7UAkVg3FjnEwpN6U9f6gG861ZDampgay5lDhjhKHSZ4V5WH4CAVbKwYBpenqD3oFNNdE2jWSAbG8qArVrZtNx3OjXgVDWytGsKqQiA1wWgbSKZ/o9lo0Y5UnjcCMqHBUNnS1Ivzm+Rpwsq4nrjvZXCgNK2rN8ak9FLImDnYYxy+FW0dIjqkGGRJtTtNlCnN2WzbNDHayh7gIyj3kZa6JM2lDUyesgzNeg0Fg90n1p60K076Rz2W0eCTc05x1ylZyM+nGuERFI6pOM69eKgmTQGbaHZZ2rhkpkd6Zay5qSDaK2g3mlI1ZJ0zNZrPevJTVwydH0KplVmHYjQRvcFFi5puHKt8rAOufnUo35GFOFawLxwF+OZU3LWbcjf4p76wbJoKwCegEn0HoguJPp2oB2ol+VftsXpHaHX5WJdrslNe+I+UfkrtYdW/VIxEz902ihbF96bzAiMb4KN5Tv6y4qpEXQLlIxqB3rwoL84FEGPb9+yga9vlVIi0wcM+Htl0+UFuNxSaWOIvVDHEEEGCMUOmMwKAjmTlOd6qkHuTWR3CFEIQG5jP0/eesEwaERSQceIzjH05ynCttQmH0jCs4TlMXg1H7VJJDYxoO/pKAJMkkzc3Pqgk3zm+rpAfOvlG7r5RY0PUIamDCto1xSDcBWq2DZmZBrN6njjcIkK0ME41E3yApHYphq3f4YtduEjeFKObuzf/Kd08wVTGTWKTF8YrQYK+JtDWxWmv56pbUktiReYkT1xwU7Z8HhTn2XG2m0mvD99Err+HIHmD/OibHwa1gRBp7YpMfQiJqIOUSLcZTcftHHHKvvTtzUqUCDr4UucK5Y66JTx/mMqXUytPyL4p9Tw2uBP3E52BryJHus3NMTF/zB6AhInP8AuKHuqCTlxjARXAR6JVUIPy7xzy5jsq27mlx3GkNwDiCQOJAAPOFmUjI615/lLoGGuCZwSI44ce3dIO1TXVJSnEYGcdVonvV4cR+Fm3XsmXchbO4xvjwSPq95IOUE61fWSJp71ujh9aF1L9NdOyW/GHdRKTTUSJGIz4I4Or3iThJgYDhy6qJSOOqIJRwutC4iRUTRwtIkGCBeoBriJuoJJMmSeabROIHEzkaUFzEdRapTEEGoaRECv3Z1wTJJERxrjyWh3Tu7sg7p3pIMul1WwBA3d0QZrJmsDKETigHCEkIDcnD4SGuap9r87869/RSBeute6qpBWj3lwGYAaYpNSROLjccg1YqiKpBTBWlOZHuk00TbFJmxtnH2+tDwRjkmGkLRkgmpxmDdQwrdjPj9+qcKmwUt+dfgLkbMANyNde6h7QP8fX8ZYY2XF2u0OPun3iedG3eJzv3j4lZlpr6+9uiHnHE1MRjytjKtzpFYprmVK2YCZ56omSOZ4Y8T+knvOOh/D6pAnWmsZ8b+x9VE5/sV13Sn9oJmUwCZQ4zGvTugtPavt+QgC4vkBjQie6QQUgMx0VEX6a9EnDjXrXjXVUlEGGpy/IHykbWtjz669qbWJ4dlEcP0gCMR14JIAT/vygFOqpgW10hGOddZqQEAyNVVHCorgKRHSO0pOMxSI48SceeCQw+KazQFB1MKWEKFRvn+c+6I1rkgET/a/wARHH4RFML2r3yjqm0kVBIIsRSCK4YoCg77YpeR9ok4RvXAjC090iZrMm1Z9zRSXTM1Oc6mUgEA5QntWQYMYG4xEj0KEBydpdQShCupS2DelKUueP5V/wDHkckkJKBaqaEISS5LGT0GQz/d1q8kAZYeo+ChCsv6lu23eeCxdZCEjIMpPE/31V7OXA0GJmxFh6H3SQkGO0vS2AmY6wPZSCIJytTOddcIqIQCcZxOQ5arzKfsfgxrmhCICKUIQko8oMiKg0ykUuJHoFEXgyM88jWChCQDfwkRrshCAQAi4m0VmIvaIwvNUGNeuuKaEAnVkx7JsHCainoOCEICN3LWKYFMEIQDBEWMyIrQCsyIqSYgzSDQzICeHL9oQgE9sU9u6RQhAMOpBmBMVsTH4QEIRDPdKaEKif/Z)
---
4. [liens vers google](https://www.google.com)
---
""")

file = st.file_uploader("Choose a file")
if file is not None:
        df = pd.read_csv(file)
        st.write(df.head())
        selected_column = st.selectbox("Column",df.columns)
        input = st.text_input("Value filter")
        filtered_df = df[df[selected_column]==input]
        st.write(filtered_df)

        st.subheader("Histogram")
        col1, col2 = st.columns(2)
        with col1:
                bins = st.slider("Number of bars",min_value = 1, max_value = 200 )
        with col2:
                x_axis = st.selectbox("x axis", df.columns)
                fig,ax = plt.subplots()
                ax.hist(df[x_axis], bins)
                st.pyplot(fig)

        st.subheader("Chart")
        graph_type = st.selectbox("graph type",["Ligne", "Barre", "Nuage de points"])

        col1, col2 = st.columns(2)
        with col1:
                x_axis = st.selectbox("x axis",df.columns,key="x axis line")
        with col2:
                y_axis = st.selectbox("y axis",df.columns,key="y axis line")
        fig,ax = plt.subplots()
                
        if graph_type == "Ligne":
                ax.plot(x_axis, y_axis, data = df)
        if graph_type == "Barre":
                ax.bar(x_axis, y_axis, data = df)
        if graph_type == "Nuage de points":
                ax.scatter(x_axis, y_axis, data = df)

        ax.set(xlabel = x_axis, ylabel = y_axis)
        st.pyplot(fig)
                

# Les widgets Streamlit exécutent automatiquement le script
# de haut en bas. Comme ce bouton n'est connecté à aucune
# autre logique, il ne fait que renvoyer un résultat vide.

st.button("Re-run")