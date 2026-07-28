# Example — `analyze-chapter` output, annotated by the author

> **Condensed sample.** A real analysis covers all 14 categories; this shows four, plus the verdict — enough to see the form. The manuscript is in Brazilian Portuguese, so the analysis is too (output-language convention). The `**R:**` lines are the author's — added *after* the analysis was generated. That annotation layer is the heart of the system.
>
> **On the numbers.** The quotes, the annotations, and the outcome are from the real session. The **density figures are illustrative**: that session predated the per-1k unit and recorded densities on the old qualitative scale, and the chapter has not been re-counted since. Treat them as showing the *shape* of a density report, not as measurements. Every figure in a live analysis comes from an actual count.

---

# Análise — Capítulo 01.01: A Estrada Termina Aqui

**Extensão:** 3.240 palavras
**Densidade do capítulo:** 14,2/1k — teto 8,0/1k. Capítulo de abertura: estabelece a voz, e por isso carrega muitos dos tiques que vão se repetir.
**Prioridade:** Crítica. É a primeira página que o leitor lê.
**Acima do teto:** cat. 1 (3,4/1k), cat. 3 (2,8/1k), cat. 4 (1,9/1k), cat. 11 (4,0/1k)

---

## 1. Antíteses binárias ("Não X. Y." e variantes)

1. **"iam e vinham de lugar nenhum para qualquer lugar"** — Paralelismo automático. Sugestão: "iam e vinham sem destino" ou cortar metade.
   **R:** essa frase é humana, eu mesmo escrevi, vou deixar.

2. **"Não por curiosidade. Pelo tom, era inventário."** — Substituir: "O tom era de quem cataloga, não de quem pergunta."
   **R:** alterei

3. **"Pessoas com problemas não pedem, mas exigem coisas ou fazem perguntas."** — Aforismo em antítese. Reescrever: "Quem tem problema exige; quem só está cansado, pede."
   **R:** alterei

4. **"Era verdade e era vago"** — Paralelismo curto. Aceitável.
   **R:** eu gostei desse, mantive tbm

**Ocorrências: 11 | Densidade: 3,4/1k | Teto: 2,0/1k | Meta: cortar 5**
**Resultado do autor: mantive 3.**

---

## 3. Hedging filosófico

1. **"Talvez estivessem acostumados com viajantes [...] Ou simplesmente talvez não se importassem. Talvez eu estivesse cansado demais..."** — **TRÊS "talvez" empilhados.** Marcador mais forte do capítulo. Comprometer-se com uma.
   **R:** eu alterei muita coisa nesse parágrafo, averiguar

2. **"Ia ser uma noite longa de perguntas, ou não."** — Cortar o "ou não".
   **R:** eu gosto de escrever `ou não` e `ou {os dois, ambos}`, é uma marca minha, mas se estiver muito ruim, me avise, eu altero.

> *↑ This annotation became a permanent entry in `persona.md` § Personal signatures. No later analysis flags "ou não" again.*

---

## 4. Meta-comentário irônico

1. **"Depois de (muitos) anos nesse trabalho"** — O parêntese "(muitos)" é tique LLM forte. Eliminar parêntese.
   **R:** removi o (muitos)

2. **"Boa pergunta. Quase boa demais."** — Tique forte. Reescrever.
   **R:** troquei para "Excelente pergunta"

3. **"aliás, onde estão as crianças?"** — Auto-interrupção. Tique.
   **R:** por hora, eu mantive, eu gostei. É um tique forte?

> *↑ A direct question. `review-revision` answered it explicitly in the next session ("leve, não forte — uma vez por capítulo é estilo") — and the construction was confirmed as a signature.*

---

## 9. Diálogo simétrico

**Cena pedindo cama:**
> — Tem quarto?
> — Tem cama.
> — Isso é um sim?
> — É uma cama.

→ **Exemplo perfeito do ping-pong simétrico.** Refazer com gesto do taverneiro entre falas e talvez uma resposta com mais que duas palavras.
   **R:** eu refiz, aguardo avaliação.

> *↑ The rewrite over-corrected — too much narrative commentary between lines. `review-revision` flagged it as an "inverted problem" and suggested keeping one gesture, not two. That failure mode is now codified in the framework (category 9).*

---

## VEREDITO

**Top 5 prioridades:**

1. Trio de "talvez" empilhados — comprometer-se com uma.
2. Lista de cinco "sem" do caderno — cortar para duas.
3. Diálogo "tem quarto? / tem cama" — refazer com textura.
4. Eliminar o "(muitos)" parentético.
5. Cortar três tríades adjetivais.

**Manter intactos (são tese):**
- "Eu sempre encontro." — eco estrutural com o final do livro.

**Tempo estimado:** 2–3 horas.
**Sensação alvo:** alguém observando, não performando observação.

---

## Outcome (recorded in `revision-log.md`)

**Density:** 14,2/1k → 5,8/1k after one revision pass (ceiling 8,0/1k). One category still over: em-dashes, 2,4/1k against a 2,0/1k ceiling.
**Decisions:** most accepted; 6 rejected — 4 of which became permanent persona signatures.
**Review notes:** author's rewrites frequently *beat* the suggestions (e.g. the beer line: *"amarga e de péssima qualidade, o que é um elogio para um lugar como esse"* — entirely his, better than anything proposed). 4 introduced errors caught (agreement, wrong word, typo). One inverted problem flagged.

That last line is the system working as designed: **the analysis proposes, the author surpasses, the reviewer catches what revision broke, and every decision compounds into the next chapter's baseline.**
