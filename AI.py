import g4f, promts


def promt_create(promt_type:str, que_count:int = 10):
  if promt_type=="test":
    promt=promts.TEST_PROMT.replace("{count}",str(que_count))
  elif promt_type=="summarize":
    promt=promts.SUMMARIZE_PROMT
  elif promt_type=="terms":
    promt=promts.TERMS_PROMT
  return promt



def main_gpt_ask(text:str, promt:str)->str:
  response=g4f.ChatCompletion.create(
    model=g4f.models.gpt_35_turbo,
    messages = [{"role":"user", "content":f"{promt} {text}",}],
  )

  return response
