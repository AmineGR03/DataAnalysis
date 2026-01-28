# Résumé Complet - Chapitre 5 : Lois de Probabilité

## 1. VARIABLES ALÉATOIRES

### 1.1 Définition

Une **variable aléatoire** est une fonction qui associe à chaque issue d'une expérience aléatoire un nombre réel.

### 1.2 Types de variables aléatoires

- **Discrète** : Prend un nombre fini ou dénombrable de valeurs isolées
- **Continue** : Peut prendre une infinité de valeurs sur un intervalle

---

## 2. VARIABLES ALÉATOIRES DISCRÈTES

### 2.1 Fonction de masse de probabilité (fmp)

Pour une variable aléatoire discrète X, la fonction de masse de probabilité est :

\[
p(x) = P(X = x)
\]

#### Propriétés

1. \(p(x) \geq 0\) pour tout \(x\)
2. \(\sum_{x} p(x) = 1\)

### 2.2 Espérance (moyenne)

\[
E(X) = \sum_{x} x \cdot p(x)
\]

L'espérance représente la **valeur moyenne attendue** de X.

### 2.3 Variance

\[
Var(X) = E[(X - E(X))^2] = E(X^2) - [E(X)]^2
\]

où :
\[
E(X^2) = \sum_{x} x^2 \cdot p(x)
\]

### 2.4 Écart-type

\[
\sigma(X) = \sqrt{Var(X)}
\]

---

## 3. VARIABLES ALÉATOIRES CONTINUES

### 3.1 Fonction de densité de probabilité (fdp)

Pour une variable aléatoire continue X, la fonction de densité de probabilité est notée \(f(x)\).

#### Propriétés

1. \(f(x) \geq 0\) pour tout \(x\)
2. \(\int_{-\infty}^{+\infty} f(x)dx = 1\)

### 3.2 Probabilité sur un intervalle

\[
P(a \leq X \leq b) = \int_{a}^{b} f(x)dx
\]

### 3.3 Espérance

\[
E(X) = \int_{-\infty}^{+\infty} x \cdot f(x)dx
\]

### 3.4 Variance

\[
Var(X) = \int_{-\infty}^{+\infty} (x - E(X))^2 f(x)dx = E(X^2) - [E(X)]^2
\]

où :
\[
E(X^2) = \int_{-\infty}^{+\infty} x^2 \cdot f(x)dx
\]

### 3.5 Écart-type

\[
\sigma(X) = \sqrt{Var(X)}
\]

---

## 4. FONCTION DE RÉPARTITION

### 4.1 Définition

La fonction de répartition d'une variable aléatoire X est :

\[
F(x) = P(X \leq x)
\]

### 4.2 Propriétés

1. \(F\) est croissante
2. \(\lim_{x \to -\infty} F(x) = 0\)
3. \(\lim_{x \to +\infty} F(x) = 1\)
4. \(F\) est continue à droite

### 4.3 Relation avec la densité (cas continu)

\[
F(x) = \int_{-\infty}^{x} f(t)dt
\]

et donc :

\[
f(x) = \frac{dF(x)}{dx}
\]

---

## 5. LOIS DE PROBABILITÉ DISCRÈTES

### 5.1 Loi de Bernoulli

#### Définition

La loi de Bernoulli modélise une expérience aléatoire avec deux résultats possibles :
- **Succès** : \(X = 1\) (probabilité \(p\))
- **Échec** : \(X = 0\) (probabilité \(1-p\))

#### Paramètre

- \(p\) : probabilité de succès, où \(0 \leq p \leq 1\)

#### Fonction de masse de probabilité

\[
P(X = x) = p^x(1-p)^{1-x}, \quad x \in \{0, 1\}
\]

ou de manière équivalente :
- \(P(X = 1) = p\)
- \(P(X = 0) = 1-p\)

#### Espérance et variance

\[
E(X) = p, \quad Var(X) = p(1-p)
\]

#### Notation

\[
X \sim \text{Ber}(p)
\]

---

### 5.2 Loi Binomiale

#### Définition

La loi binomiale modélise le **nombre de succès** dans \(n\) essais indépendants de Bernoulli, chacun ayant une probabilité de succès \(p\).

#### Paramètres

- \(n\) : nombre d'essais
- \(p\) : probabilité de succès à chaque essai

#### Fonction de masse de probabilité

\[
P(X = k) = \binom{n}{k} p^k(1-p)^{n-k}, \quad k = 0, 1, 2, ..., n
\]

où le coefficient binomial est :

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

#### Espérance et variance

\[
E(X) = np, \quad Var(X) = np(1-p)
\]

#### Notation

\[
X \sim \text{B}(n, p)
\]

#### Relation avec Bernoulli

Si \(X_1, X_2, ..., X_n\) sont \(n\) variables de Bernoulli indépendantes avec \(P(X_i = 1) = p\), alors :

\[
Y = \sum_{i=1}^{n} X_i \sim \text{B}(n, p)
\]

---

## 6. LOIS DE PROBABILITÉ CONTINUES

### 6.1 Loi Exponentielle

#### Définition

La loi exponentielle modélise le **temps entre deux événements** dans un processus de Poisson (ex: temps d'attente entre des appels).

#### Paramètre

- \(\lambda > 0\) : taux (paramètre d'échelle)

#### Fonction de densité de probabilité

\begin{align}
f_X(x) = \lambda e^{-\lambda x}, \quad x \geq 0
\end{align}

#### Fonction de répartition

\begin{align}
F_X(x) = 1 - e^{-\lambda x}, \quad x \geq 0
\end{align}

#### Espérance et variance

\begin{align}
E(X) = \frac{1}{\lambda}, \quad Var(X) = \frac{1}{\lambda^2}
\end{align}

#### Propriété importante : Absence de mémoire

\[
P(X > s + t | X > s) = P(X > t)
\]

#### Notation

\[
X \sim \text{Exp}(\lambda)
\]

---

### 6.2 Loi Normale (Gaussienne)

#### Définition

La loi normale est une loi de probabilité continue, souvent utilisée pour modéliser des phénomènes naturels (erreurs de mesure, tailles, poids, etc.).

#### Paramètres

- \(\mu\) : moyenne (ou espérance)
- \(\sigma > 0\) : écart-type (mesure la dispersion)

#### Fonction de densité de probabilité

\begin{align}
f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}
\end{align}

#### Propriétés

1. **Symétrie** : La courbe est symétrique par rapport à la moyenne \(\mu\)
2. **Espérance et variance** :
   \[
   E(X) = \mu, \quad Var(X) = \sigma^2
   \]

#### Fonction de répartition

\begin{align}
F_X(x) = P(X \leq x) = \frac{1}{2}\left[1 + \text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
\end{align}

où la fonction d'erreur est :

\begin{align}
\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} \, dt
\end{align}

#### Notation

\[
X \sim N(\mu, \sigma^2)
\]

---

### 6.3 Loi Normale Centrée Réduite

#### Définition

Si \(X \sim N(\mu, \sigma^2)\), alors la variable centrée réduite :

\[
Z = \frac{X - \mu}{\sigma} \sim N(0, 1)
\]

#### Fonction de densité

\begin{align}
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}, \quad z \in \mathbb{R}
\end{align}

#### Fonction de répartition

\begin{align}
\Phi(z) = P(Z \leq z) = \int_{-\infty}^{z} \phi(t) \, dt
\end{align}

#### Propriétés importantes

- \(\Phi(-z) = 1 - \Phi(z)\)
- \(P(a \leq Z \leq b) = \Phi(b) - \Phi(a)\)
- Pour \(X \sim N(\mu, \sigma^2)\) : \(P(a \leq X \leq b) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right)\)

#### Règle des 3 sigmas

Pour \(X \sim N(\mu, \sigma^2)\) :
- \(P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 0.68\) (68%)
- \(P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 0.95\) (95%)
- \(P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 0.997\) (99.7%)

---

## 7. OPÉRATIONS SUR LES VARIABLES ALÉATOIRES

### 7.1 Transformation linéaire

Si \(Y = aX + b\) où \(a, b\) sont des constantes :

\[
E(Y) = aE(X) + b, \quad Var(Y) = a^2 Var(X)
\]

### 7.2 Somme de variables indépendantes

Si \(X\) et \(Y\) sont indépendantes :

\[
E(X + Y) = E(X) + E(Y)
\]

\[
Var(X + Y) = Var(X) + Var(Y)
\]

### 7.3 Produit de variables indépendantes

Si \(X\) et \(Y\) sont indépendantes :

\[
E(XY) = E(X)E(Y)
\]

---

## 8. RÉSUMÉ DES FORMULES CLÉS

### Variables discrètes

| Concept | Formule |
|---------|---------|
| Espérance | \(E(X) = \sum_x x \cdot p(x)\) |
| Variance | \(Var(X) = E(X^2) - [E(X)]^2\) |
| Écart-type | \(\sigma(X) = \sqrt{Var(X)}\) |

### Variables continues

| Concept | Formule |
|---------|---------|
| Probabilité | \(P(a \leq X \leq b) = \int_a^b f(x)dx\) |
| Espérance | \(E(X) = \int_{-\infty}^{+\infty} x f(x)dx\) |
| Variance | \(Var(X) = E(X^2) - [E(X)]^2\) |
| Écart-type | \(\sigma(X) = \sqrt{Var(X)}\) |

### Lois discrètes

| Loi | Paramètres | \(E(X)\) | \(Var(X)\) |
|-----|------------|----------|------------|
| Bernoulli | \(p\) | \(p\) | \(p(1-p)\) |
| Binomiale | \(n, p\) | \(np\) | \(np(1-p)\) |

### Lois continues

| Loi | Paramètres | \(E(X)\) | \(Var(X)\) |
|-----|------------|----------|------------|
| Exponentielle | \(\lambda\) | \(\frac{1}{\lambda}\) | \(\frac{1}{\lambda^2}\) |
| Normale | \(\mu, \sigma^2\) | \(\mu\) | \(\sigma^2\) |

---

## 9. EXERCICE D'APPLICATION

### Énoncé

Une entreprise fabrique des composants électroniques. On sait que :
- La probabilité qu'un composant soit défectueux est \(p = 0.05\)
- La durée de vie d'un composant (en heures) suit une loi exponentielle de paramètre \(\lambda = 0.001\) (1 composant par 1000 heures en moyenne)
- Le poids d'un composant (en grammes) suit une loi normale \(N(50, 4)\) (moyenne 50g, variance 4g²)

**Questions** :

1. **Loi Binomiale** : Sur un lot de 100 composants, quelle est la probabilité qu'exactement 3 composants soient défectueux ? Quelle est la probabilité qu'au moins 2 composants soient défectueux ?

2. **Loi Exponentielle** : 
   - Quelle est la probabilité qu'un composant dure plus de 2000 heures ?
   - Quelle est la durée de vie moyenne d'un composant ?
   - Quelle est la probabilité qu'un composant dure entre 500 et 1500 heures ?

3. **Loi Normale** :
   - Quelle est la probabilité qu'un composant pèse moins de 48 grammes ?
   - Quelle est la probabilité qu'un composant pèse entre 48 et 52 grammes ?
   - Quel poids ne sera dépassé que par 10% des composants ?

### Solution guidée

#### 1. Loi Binomiale

Soit \(X\) le nombre de composants défectueux parmi 100. Alors \(X \sim B(100, 0.05)\).

**a) Probabilité d'exactement 3 défectueux**

\[
P(X = 3) = \binom{100}{3} (0.05)^3 (0.95)^{97}
\]

\[
= \frac{100!}{3!97!} \times 0.000125 \times 0.95^{97}
\]

\[
= \frac{100 \times 99 \times 98}{3 \times 2 \times 1} \times 0.000125 \times 0.95^{97}
\]

\[
= 161700 \times 0.000125 \times 0.95^{97}
\]

En utilisant une calculatrice ou un logiciel :
\[
P(X = 3) \approx 0.1396 \text{ (environ 14%)}
\]

**b) Probabilité d'au moins 2 défectueux**

\[
P(X \geq 2) = 1 - P(X = 0) - P(X = 1)
\]

\[
P(X = 0) = \binom{100}{0} (0.05)^0 (0.95)^{100} = (0.95)^{100} \approx 0.0059
\]

\[
P(X = 1) = \binom{100}{1} (0.05)^1 (0.95)^{99} = 100 \times 0.05 \times (0.95)^{99} \approx 0.0312
\]

\[
P(X \geq 2) = 1 - 0.0059 - 0.0312 = 0.9629 \text{ (environ 96.3%)}
\]

#### 2. Loi Exponentielle

Soit \(T\) la durée de vie d'un composant. Alors \(T \sim \text{Exp}(0.001)\).

**a) Probabilité que \(T > 2000\) heures**

\[
P(T > 2000) = 1 - F_T(2000) = 1 - (1 - e^{-0.001 \times 2000}) = e^{-2} \approx 0.1353
\]

**b) Durée de vie moyenne**

\[
E(T) = \frac{1}{\lambda} = \frac{1}{0.001} = 1000 \text{ heures}
\]

**c) Probabilité que \(500 \leq T \leq 1500\)**

\[
P(500 \leq T \leq 1500) = F_T(1500) - F_T(500)
\]

\[
= (1 - e^{-0.001 \times 1500}) - (1 - e^{-0.001 \times 500})
\]

\[
= e^{-0.5} - e^{-1.5} \approx 0.6065 - 0.2231 = 0.3834
\]

#### 3. Loi Normale

Soit \(W\) le poids d'un composant. Alors \(W \sim N(50, 4)\), donc \(\mu = 50\) et \(\sigma = 2\).

**a) Probabilité que \(W < 48\) grammes**

On standardise : \(Z = \frac{W - 50}{2}\)

\[
P(W < 48) = P\left(Z < \frac{48 - 50}{2}\right) = P(Z < -1) = \Phi(-1)
\]

\[
= 1 - \Phi(1) = 1 - 0.8413 = 0.1587 \text{ (environ 15.9%)}
\]

**b) Probabilité que \(48 \leq W \leq 52\)**

\[
P(48 \leq W \leq 52) = P\left(\frac{48-50}{2} \leq Z \leq \frac{52-50}{2}\right)
\]

\[
= P(-1 \leq Z \leq 1) = \Phi(1) - \Phi(-1) = \Phi(1) - (1 - \Phi(1))
\]

\[
= 2\Phi(1) - 1 = 2 \times 0.8413 - 1 = 0.6826 \text{ (environ 68.3%)}
\]

**c) Poids tel que \(P(W > w) = 0.10\)**

On cherche \(w\) tel que \(P(W > w) = 0.10\), donc \(P(W \leq w) = 0.90\).

\[
P(W \leq w) = 0.90 \Rightarrow P\left(Z \leq \frac{w-50}{2}\right) = 0.90
\]

\[
\Rightarrow \frac{w-50}{2} = \Phi^{-1}(0.90) \approx 1.28
\]

\[
\Rightarrow w = 50 + 2 \times 1.28 = 52.56 \text{ grammes}
\]

**Réponse** : 10% des composants pèsent plus de **52.56 grammes**.

---

## 10. TABLE DE LA LOI NORMALE STANDARD (Valeurs importantes)

| z | \(\Phi(z)\) | z | \(\Phi(z)\) |
|---|-------------|---|-------------|
| 0.0 | 0.5000 | 1.0 | 0.8413 |
| 0.5 | 0.6915 | 1.5 | 0.9332 |
| 0.67 | 0.7486 | 1.96 | 0.9750 |
| 0.84 | 0.7995 | 2.0 | 0.9772 |
| 0.90 | 0.8159 | 2.5 | 0.9938 |
| | | 3.0 | 0.9987 |

**Valeurs critiques importantes** :
- \(\Phi^{-1}(0.95) = 1.645\)
- \(\Phi^{-1}(0.975) = 1.96\)
- \(\Phi^{-1}(0.99) = 2.326\)

