# Formules LaTeX - Référence Rapide

Ce document contient toutes les formules importantes des chapitres sous forme LaTeX pour référence rapide.

## Chapitre 3 : Corrélation et Régression

### Coefficient de corrélation de Pearson

```latex
\begin{align}
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \sum_{i=1}^{n}(y_i - \bar{y})^2}}
\end{align}
```

### Régression linéaire simple

**Modèle :**
```latex
\begin{align}
Y = \beta_0 + \beta_1 X + \varepsilon
\end{align}
```

**Estimateurs :**
```latex
\begin{align}
\hat{\beta}_1 &= \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} \\
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1\bar{x}
\end{align}
```

**Résidus :**
```latex
\begin{align}
e_i = y_i - \hat{y}_i
\end{align}
```

**R² :**
```latex
\begin{align}
R^2 = \frac{SS_{\text{exp}}}{SS_{\text{tot}}} = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\end{align}
```

### Régression linéaire multiple

**Modèle matriciel :**
```latex
\begin{align}
\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}
\end{align}
```

**Estimateur MCO :**
```latex
\begin{align}
\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
\end{align}
```

**R² ajusté :**
```latex
\begin{align}
R^2_{\text{ajusté}} = 1 - (n-1)\frac{1-R^2}{n-p-1}
\end{align}
```

---

## Chapitre 5 : Lois de Probabilité

### Variables discrètes

**Espérance :**
```latex
\begin{align}
E(X) = \sum_{x} x \cdot p(x)
\end{align}
```

**Variance :**
```latex
\begin{align}
Var(X) = E[(X - E(X))^2] = E(X^2) - [E(X)]^2
\end{align}
```

**Écart-type :**
```latex
\begin{align}
\sigma(X) = \sqrt{Var(X)}
\end{align}
```

### Variables continues

**Probabilité :**
```latex
\begin{align}
P(a \leq X \leq b) = \int_{a}^{b} f(x)dx
\end{align}
```

**Espérance :**
```latex
\begin{align}
E(X) = \int_{-\infty}^{+\infty} x \cdot f(x)dx
\end{align}
```

**Variance :**
```latex
\begin{align}
Var(X) = \int_{-\infty}^{+\infty} (x - E(X))^2 f(x)dx = E(X^2) - [E(X)]^2
\end{align}
```

### Loi de Bernoulli

```latex
\begin{align}
P(X = x) = p^x(1-p)^{1-x}, \quad x \in \{0, 1\}
\end{align}
```

```latex
\begin{align}
E(X) = p, \quad Var(X) = p(1-p)
\end{align}
```

### Loi Binomiale

```latex
\begin{align}
P(X = k) = \binom{n}{k} p^k(1-p)^{n-k}, \quad k = 0, 1, 2, ..., n
\end{align}
```

```latex
\begin{align}
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\end{align}
```

```latex
\begin{align}
E(X) = np, \quad Var(X) = np(1-p)
\end{align}
```

### Loi Exponentielle

**Densité :**
```latex
\begin{align}
f_X(x) = \lambda e^{-\lambda x}, \quad x \geq 0
\end{align}
```

**Répartition :**
```latex
\begin{align}
F_X(x) = 1 - e^{-\lambda x}, \quad x \geq 0
\end{align}
```

**Espérance et variance :**
```latex
\begin{align}
E(X) = \frac{1}{\lambda}, \quad Var(X) = \frac{1}{\lambda^2}
\end{align}
```

### Loi Normale

**Densité :**
```latex
\begin{align}
f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}
\end{align}
```

**Répartition :**
```latex
\begin{align}
F_X(x) = P(X \leq x) = \frac{1}{2}\left[1 + \text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
\end{align}
```

**Fonction d'erreur :**
```latex
\begin{align}
\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2} \, dt
\end{align}
```

**Loi normale centrée réduite :**
```latex
\begin{align}
Z = \frac{X - \mu}{\sigma} \sim N(0, 1)
\end{align}
```

**Densité standard :**
```latex
\begin{align}
\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}, \quad z \in \mathbb{R}
\end{align}
```

**Répartition standard :**
```latex
\begin{align}
\Phi(z) = P(Z \leq z) = \int_{-\infty}^{z} \phi(t) \, dt
\end{align}
```

---

## Chapitre 5 (Suite) : Tests d'Hypothèses

### Test sur la moyenne (variance connue)

```latex
\begin{align}
Z_0 = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1)
\end{align}
```

**Règle de décision bilatérale :**
- Rejeter \(H_0\) si \(|Z_0| > z_{\alpha/2}\)
- Accepter \(H_0\) si \(|Z_0| \leq z_{\alpha/2}\)

### Test sur la moyenne (variance inconnue)

```latex
\begin{align}
T_0 = \frac{\bar{X} - \mu_0}{S/\sqrt{n}} \sim t_{n-1}
\end{align}
```

où :
```latex
\begin{align}
S = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
\end{align}
```

**Règle de décision bilatérale :**
- Rejeter \(H_0\) si \(|T_0| > t_{\alpha/2; n-1}\)
- Accepter \(H_0\) si \(|T_0| \leq t_{\alpha/2; n-1}\)

### P-value

**Variance connue (bilatéral) :**
```latex
\begin{align}
PV = 2(1 - \Phi(|z_0|))
\end{align}
```

**Variance inconnue (bilatéral) :**
```latex
\begin{align}
PV = 2P(T > |t_0|) \quad \text{avec } T \sim t_{n-1}
\end{align}
```

### Test d'ajustement du khi-deux

```latex
\begin{align}
\chi_0^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i} \sim \chi_{k-p-1}^2
\end{align}
```

où :
- \(k\) : nombre de classes
- \(p\) : nombre de paramètres estimés

**Effectifs attendus :**
```latex
\begin{align}
E_i = n \times p_i^{(0)}
\end{align}
```

où :
```latex
\begin{align}
p_i^{(0)} = P(X \in V_i | H_0 \text{ est vraie})
\end{align}
```

---

## Chapitre 6 : Analyse en Composantes Principales (ACP)

### Matrices

**Matrice centrée :**
```latex
\begin{align}
a_{ij} = x_{ij} - \bar{x}_j
\end{align}
```

**Matrice centrée réduite :**
```latex
\begin{align}
m_{ij} &= \frac{x_{ij} - \bar{x}_j}{\sigma_j} \\
\sigma_j &= \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_{ij} - \bar{x}_j)^2}
\end{align}
```

**Matrice des variances-covariances :**
```latex
\begin{align}
\mathbf{V} = \frac{1}{n} \mathbf{M}_c^T \mathbf{M}_c
\end{align}
```

**Matrice des corrélations :**
```latex
\begin{align}
\mathbf{U} = \frac{1}{n} \mathbf{M}_{cr}^T \mathbf{M}_{cr}
\end{align}
```

### Inertie

```latex
\begin{align}
I_g = \frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{p}(x_{ik} - \bar{x}_k)^2 = \sum_{k=1}^{p} \sigma_k^2
\end{align}
```

Pour données centrées-réduites : \(I_g = p\)

### Valeurs et vecteurs propres

```latex
\begin{align}
\mathbf{U}\mathbf{u}_k = \lambda_k \mathbf{u}_k, \quad k = 1, ..., p
\end{align}
```

```latex
\begin{align}
P(\lambda) = \det(\mathbf{U} - \lambda \mathbf{I}_p) = 0
\end{align}
```

```latex
\begin{align}
\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0
\end{align}
```

### Composantes principales

```latex
\begin{align}
\mathbf{C}_1 &= \mathbf{M}_{cr} \mathbf{u}_1 \\
\mathbf{C}_2 &= \mathbf{M}_{cr} \mathbf{u}_2 \\
&\vdots \\
\mathbf{C}_k &= \mathbf{M}_{cr} \mathbf{u}_k
\end{align}
```

### Inertie expliquée

**Inertie d'un axe :**
```latex
\begin{align}
\text{Inertie axe } k = \frac{\lambda_k}{\sum_{i=1}^{p} \lambda_i} = \frac{\lambda_k}{I_g}
\end{align}
```

**Inertie cumulée :**
```latex
\begin{align}
\text{Inertie cumulée} = \frac{\sum_{i=1}^{k} \lambda_i}{\sum_{i=1}^{p} \lambda_i}
\end{align}
```

### Contributions

**Contribution d'un individu :**
```latex
\begin{align}
\text{CONTR}(i) = \frac{1}{np} \sum_{j=1}^{p} m_{ij}^2
\end{align}
```

**Contribution d'une variable :**
```latex
\begin{align}
\text{CONTR}(X_j) = \frac{1}{p} \sum_{i=1}^{n} \frac{m_{ij}^2}{I_g}
\end{align}
```

**Contribution d'un individu à un axe :**
```latex
\begin{align}
\text{CONTR}(i, \text{axe } k) = \frac{1}{n} \frac{C_{ik}^2}{\lambda_k}
\end{align}
```

---

## Opérations sur matrices

### Multiplication

```latex
\begin{align}
(\mathbf{AB})_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}
\end{align}
```

### Transposée

```latex
\begin{align}
(\mathbf{A}^T)_{ij} = a_{ji}
\end{align}
```

### Propriétés

- \((\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T\)
- \((\mathbf{A}^T)^T = \mathbf{A}\)
- \((\mathbf{A}^{-1})^T = (\mathbf{A}^T)^{-1}\)
- \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\) (si les inverses existent)

### Déterminant (2×2)

```latex
\begin{align}
\det(\mathbf{A}) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
\end{align}
```

### Déterminant (3×3)

```latex
\begin{align}
\det(\mathbf{A}) = a(ei - fh) - b(di - fg) + c(dh - eg)
\end{align}
```

---

## Notes d'utilisation

- Utilisez `\begin{align}...\end{align}` pour les équations multi-lignes
- Utilisez `\text{}` pour le texte dans les formules mathématiques
- Utilisez `\,` pour un espacement fin dans les intégrales
- Les indices utilisent `_` et les exposants `^`
- Les vecteurs en gras utilisent `\mathbf{}` ou `\boldsymbol{}`
- Les matrices utilisent `\mathbf{}` ou `\boldsymbol{}`

