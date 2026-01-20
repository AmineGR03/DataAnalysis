# Résumé Complet - Chapitre 5 (Suite) : Tests d'Hypothèses

## 1. INTRODUCTION

### 1.1 Définition

Un **test d'hypothèse** est une méthode statistique permettant de vérifier :
- La valeur d'un paramètre (moyenne, variance, proportion, etc.)
- L'égalité des paramètres de deux distributions
- La forme d'une distribution

### 1.2 Types d'hypothèses

- **Hypothèse paramétrique** : concerne la valeur d'un paramètre ou l'égalité de paramètres
- **Hypothèse non paramétrique** : concerne la forme d'une distribution

---

## 2. HYPOTHÈSES NULLE ET ALTERNATIVE

### 2.1 Définitions

On cherche à vérifier la valeur d'un paramètre inconnu \(\theta\) de la distribution d'une population \(X\).

**Hypothèse nulle** (\(H_0\)) : 
\[
H_0 : \theta = \theta_0
\]

**Hypothèse alternative** (\(H_1\)) : peut prendre l'une des formes suivantes :

1. **Bilatérale** : \(H_1 : \theta \neq \theta_0\)
2. **Unilatérale à gauche** : \(H_1 : \theta < \theta_0\)
3. **Unilatérale à droite** : \(H_1 : \theta > \theta_0\)

### 2.2 Origine de l'hypothèse nulle

L'hypothèse nulle peut provenir de :
- Expériences antérieures (vérifier si les conditions ont changé)
- Une théorie ou un modèle (vérifier si le modèle est valide)
- Spécifications techniques (vérifier la conformité)

---

## 3. ERREURS DE TYPE I ET TYPE II

### 3.1 Définitions

| Décision | Réalité : \(H_0\) vraie | Réalité : \(H_0\) fausse |
|----------|------------------------|--------------------------|
| Accepter \(H_0\) | \(1-\alpha\) (correct) | Erreur de type II (\(\beta\)) |
| Rejeter \(H_0\) | Erreur de type I (\(\alpha\)) | \(1-\beta\) (puissance) |

**Erreur de type I** :
\[
\alpha = P(\text{rejeter } H_0 | H_0 \text{ est vraie})
\]

**Erreur de type II** :
\[
\beta = P(\text{accepter } H_0 | H_0 \text{ est fausse})
\]

### 3.2 Concepts importants

- **Seuil de signification** (\(\alpha\)) : probabilité de l'erreur de type I (fixé à l'avance, souvent 0.05 ou 0.01)
- **Puissance du test** : \(1-\beta\) = probabilité de rejeter \(H_0\) si \(H_0\) est fausse

### 3.3 Remarques

- On choisit généralement \(\alpha\) petit (0.05, 0.01)
- Pour \(\alpha\) et \(n\) fixés, \(\beta = \beta(\theta)\) est une fonction du paramètre \(\theta\)
- Le graphe de \(\beta(\theta)\) est appelé **courbe caractéristique du test**
- Souvent \(\alpha < \beta\)
- Pour diminuer \(\beta\), il faut augmenter \(\alpha\) et/ou \(n\)

---

## 4. RÉGION CRITIQUE

### 4.1 Principe

Une **région critique** est une région où il est peu probable que la statistique prenne des valeurs lorsque l'hypothèse nulle est vraie.

### 4.2 Décision

- **Rejeter \(H_0\)** si la valeur calculée de la statistique est dans la région critique → **conclusion forte**
- **Ne pas rejeter (accepter) \(H_0\)** si la valeur calculée est en dehors de la région critique → **conclusion faible**

---

## 5. ÉTAPES D'EXÉCUTION D'UN TEST

1. **Formuler** \(H_0\) et \(H_1\)
2. **Choisir** \(\alpha\) (seuil de signification)
3. **Considérer** un échantillon de taille \(n\)
4. **Exécuter** le test : calculer la statistique et vérifier si elle est dans la région critique
5. **Conclure** en acceptant ou en rejetant \(H_0\)
6. (Facultatif) Calculer \(\beta\) et le risque de deuxième espèce
7. (Facultatif) Si \(\beta\) est trop élevé, indiquer un nouveau \(\alpha\) et/ou un nouveau \(n\) et recommencer

---

## 6. TESTS D'HYPOTHÈSES SUR LA MOYENNE D'UN SEUL ÉCHANTILLON

### 6.1 Test bilatéral : variance connue

#### Hypothèses

\[
H_0 : \mu = \mu_0 \quad \text{vs} \quad H_1 : \mu \neq \mu_0
\]

#### Statistique de test

\begin{align}
Z_0 = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}
\end{align}

Si \(H_0\) est vraie, alors \(Z_0 \sim N(0,1)\) (pour \(n\) grand ou si \(X \sim N(\mu, \sigma^2)\)).

#### Règle de décision

- **Rejeter \(H_0\)** si \(|Z_0| > z_{\alpha/2}\)
- **Accepter \(H_0\)** si \(|Z_0| \leq z_{\alpha/2}\)

où \(z_{\alpha/2}\) est le quantile d'ordre \(1-\alpha/2\) de la loi normale standard.

**Valeurs critiques usuelles** :
- \(\alpha = 0.05\) : \(z_{0.025} = 1.96\)
- \(\alpha = 0.01\) : \(z_{0.005} = 2.576\)

---

### 6.2 Test bilatéral : variance inconnue

#### Hypothèses

\[
H_0 : \mu = \mu_0 \quad \text{vs} \quad H_1 : \mu \neq \mu_0
\]

#### Statistique de test

\begin{align}
T_0 = \frac{\bar{X} - \mu_0}{S/\sqrt{n}}
\end{align}

où \(S\) est l'écart-type empirique :

\begin{align}
S = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
\end{align}

Si \(H_0\) est vraie et \(X \sim N(\mu, \sigma^2)\), alors \(T_0 \sim t_{n-1}\) (loi de Student à \(n-1\) degrés de liberté).

#### Règle de décision

- **Rejeter \(H_0\)** si \(|T_0| > t_{\alpha/2; n-1}\)
- **Accepter \(H_0\)** si \(|T_0| \leq t_{\alpha/2; n-1}\)

où \(t_{\alpha/2; n-1}\) est le quantile d'ordre \(1-\alpha/2\) de la loi de Student à \(n-1\) degrés de liberté.

---

### 6.3 Tests unilatéraux

#### Test unilatéral à gauche

**Hypothèses** :
\[
H_0 : \mu = \mu_0 \text{ (ou } \mu \geq \mu_0\text{)} \quad \text{vs} \quad H_1 : \mu < \mu_0
\]

**Règle de rejet** :
- Si \(\sigma\) connu : rejeter \(H_0\) si \(Z_0 < -z_{\alpha}\)
- Si \(\sigma\) inconnu : rejeter \(H_0\) si \(T_0 < -t_{\alpha; n-1}\)

#### Test unilatéral à droite

**Hypothèses** :
\[
H_0 : \mu = \mu_0 \text{ (ou } \mu \leq \mu_0\text{)} \quad \text{vs} \quad H_1 : \mu > \mu_0
\]

**Règle de rejet** :
- Si \(\sigma\) connu : rejeter \(H_0\) si \(Z_0 > z_{\alpha}\)
- Si \(\sigma\) inconnu : rejeter \(H_0\) si \(T_0 > t_{\alpha; n-1}\)

#### Tableau récapitulatif

| Test | \(H_1\) | \(\sigma\) connu | \(\sigma\) inconnu |
|------|---------|-----------------|-------------------|
| Unilatéral gauche | \(\mu < \mu_0\) | \(Z_0 < -z_{\alpha}\) | \(T_0 < -t_{\alpha; n-1}\) |
| Unilatéral droite | \(\mu > \mu_0\) | \(Z_0 > z_{\alpha}\) | \(T_0 > t_{\alpha; n-1}\) |
| Bilatéral | \(\mu \neq \mu_0\) | \(|Z_0| > z_{\alpha/2}\) | \(|T_0| > t_{\alpha/2; n-1}\) |

---

## 7. NIVEAU CRITIQUE OBSERVÉ (P-VALUE)

### 7.1 Définition

Le **niveau critique observé** (ou **P-value**, notée \(PV\)) est la valeur minimale de \(\alpha\) telle que \(H_0\) est toujours rejetée.

### 7.2 Avantages

- Une fois la P-value connue, on peut déterminer la décision pour n'importe quel seuil \(\alpha\)
- Si \(\alpha > PV\), alors \(H_0\) est rejetée
- Les logiciels donnent généralement la P-value

### 7.3 Calcul de la P-value

Soit \(Z_0\) (ou \(T_0\)) la statistique employée et \(z_0\) (ou \(t_0\)) sa valeur calculée.

#### Si \(\sigma^2\) est connue (test sur la moyenne)

- **Unilatéral gauche** (\(H_1 : \mu < \mu_0\)) : \(PV = \Phi(z_0)\)
- **Unilatéral droite** (\(H_1 : \mu > \mu_0\)) : \(PV = 1 - \Phi(z_0)\)
- **Bilatéral** (\(H_1 : \mu \neq \mu_0\)) : \(PV = 2(1 - \Phi(|z_0|))\)

où \(\Phi\) est la fonction de répartition de la loi normale standard.

#### Si \(\sigma^2\) est inconnue (test sur la moyenne)

- **Unilatéral** : \(PV = P(T > |t_0|)\) avec \(T \sim t_{n-1}\)
- **Bilatéral** : \(PV = 2P(T > |t_0|)\) avec \(T \sim t_{n-1}\)

### 7.4 Interprétation

- Si \(PV < \alpha\) : rejeter \(H_0\)
- Si \(PV \geq \alpha\) : ne pas rejeter \(H_0\)

---

## 8. TEST D'AJUSTEMENT DU KHI-DEUX (\(\chi^2\))

### 8.1 Objectif

Vérifier si les données \(x_1, ..., x_n\) proviennent d'une population distribuée selon une loi particulière \(F(x, \theta)\).

### 8.2 Hypothèses

\[
H_0 : X \sim F(x, \theta) \quad \text{vs} \quad H_1 : X \not\sim F(x, \theta)
\]

### 8.3 Méthode

#### Étape 1 : Regroupement des observations

On regroupe les observations en \(k\) classes (valeurs ou intervalles) :

| Valeurs (\(V_i\)) | \(V_1\) | \(V_2\) | ... | \(V_i\) | ... | Total |
|-------------------|---------|---------|-----|---------|-----|-------|
| Effectifs observés (\(O_i\)) | \(O_1\) | \(O_2\) | ... | \(O_i\) | ... | \(n\) |
| Effectifs attendus (\(E_i\)) | \(E_1\) | \(E_2\) | ... | \(E_i\) | ... | \(n\) |

#### Étape 2 : Calcul des effectifs attendus

\[
E_i = n \times p_i^{(0)}
\]

où :
\[
p_i^{(0)} = P(X \in V_i | H_0 \text{ est vraie}), \quad i = 1, 2, ..., k
\]

et :
\[
\sum_{i=1}^{k} p_i^{(0)} = 1
\]

**Remarque** : Si certains \(E_i\) sont petits (< 5), regrouper des classes.

#### Étape 3 : Calcul de la statistique du test

\begin{align}
\chi_0^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}
\end{align}

La statistique \(\chi_0^2\) représente une "distance" globale entre les effectifs observés et attendus.

#### Étape 4 : Distribution sous \(H_0\)

Si \(H_0\) est vraie, alors \(\chi_0^2 \sim \chi_{\nu}^2\) (loi du khi-deux) avec :

\[
\nu = k - p - 1
\]

où :
- \(k\) : nombre de classes retenues
- \(p\) : nombre de paramètres estimés

#### Étape 5 : Règle de décision

Pour un niveau critique \(\alpha\) donné :

- **Rejeter \(H_0\)** si \(\chi_0^2 > \chi_{\alpha; \nu}^2\)
- **Accepter \(H_0\)** si \(\chi_0^2 \leq \chi_{\alpha; \nu}^2\)

où \(\chi_{\alpha; \nu}^2\) est le quantile d'ordre \(1-\alpha\) de la loi \(\chi_{\nu}^2\).

---

## 9. RÉSUMÉ DES FORMULES CLÉS

### Tests sur la moyenne (variance connue)

\begin{align}
Z_0 = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} \sim N(0,1)
\end{align}

### Tests sur la moyenne (variance inconnue)

\begin{align}
T_0 = \frac{\bar{X} - \mu_0}{S/\sqrt{n}} \sim t_{n-1}
\end{align}

où :
\begin{align}
S = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
\end{align}

### Test d'ajustement du khi-deux

\begin{align}
\chi_0^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i} \sim \chi_{k-p-1}^2
\end{align}

### P-value (cas bilatéral, variance connue)

\begin{align}
PV = 2(1 - \Phi(|z_0|))
\end{align}

---

## 10. EXERCICE D'APPLICATION

### Énoncé

Une entreprise fabrique des boulons. Le cahier des charges spécifie que le diamètre moyen des boulons doit être de 10 mm avec un écart-type de 0.5 mm.

Un contrôle qualité est effectué sur un échantillon de 25 boulons. Les résultats sont les suivants :

**Diamètres mesurés (en mm)** :
9.8, 10.1, 9.9, 10.2, 9.7, 10.0, 10.3, 9.8, 10.1, 9.9, 10.0, 10.2, 9.8, 10.1, 10.0, 9.9, 10.2, 10.1, 9.8, 10.0, 10.1, 9.9, 10.2, 10.0, 9.8

**Questions** :

1. **Test bilatéral** : Au seuil de signification \(\alpha = 0.05\), peut-on conclure que le diamètre moyen est conforme aux spécifications (10 mm) ?

2. **Test unilatéral** : Au seuil \(\alpha = 0.05\), peut-on conclure que le diamètre moyen est supérieur à 10 mm ?

3. **P-value** : Calculer la P-value pour le test bilatéral.

4. **Test d'ajustement** : On souhaite vérifier si les diamètres suivent une loi normale \(N(10, 0.25)\). Les données ont été regroupées en 4 classes :

| Intervalle | [9.5, 9.75[ | [9.75, 10[ | [10, 10.25[ | [10.25, 10.5[ |
|------------|-------------|-------------|--------------|----------------|
| Effectifs observés | 3 | 8 | 10 | 4 |

Effectuer le test d'ajustement du khi-deux au seuil \(\alpha = 0.05\).

### Solution guidée

#### 1. Test bilatéral (variance connue)

**Étape 1** : Formuler les hypothèses

\[
H_0 : \mu = 10 \quad \text{vs} \quad H_1 : \mu \neq 10
\]

**Étape 2** : Calculer la moyenne de l'échantillon

\[
\bar{x} = \frac{1}{25}\sum_{i=1}^{25} x_i = \frac{249.8}{25} = 9.992 \text{ mm}
\]

**Étape 3** : Calculer la statistique de test

\[
Z_0 = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}} = \frac{9.992 - 10}{0.5/\sqrt{25}} = \frac{-0.008}{0.1} = -0.08
\]

**Étape 4** : Règle de décision

Pour \(\alpha = 0.05\), on a \(z_{0.025} = 1.96\).

\[
|Z_0| = 0.08 < 1.96
\]

**Conclusion** : On **accepte \(H_0\)** au seuil 5%. Le diamètre moyen est conforme aux spécifications.

#### 2. Test unilatéral à droite

**Étape 1** : Formuler les hypothèses

\[
H_0 : \mu \leq 10 \quad \text{vs} \quad H_1 : \mu > 10
\]

**Étape 2** : Statistique de test (même calcul)

\[
Z_0 = -0.08
\]

**Étape 3** : Règle de décision

Pour \(\alpha = 0.05\), on a \(z_{0.05} = 1.645\).

\[
Z_0 = -0.08 < 1.645
\]

**Conclusion** : On **accepte \(H_0\)** au seuil 5%. On ne peut pas conclure que le diamètre moyen est supérieur à 10 mm.

#### 3. Calcul de la P-value (test bilatéral)

\[
PV = 2(1 - \Phi(|z_0|)) = 2(1 - \Phi(0.08)) = 2(1 - 0.5319) = 2 \times 0.4681 = 0.9362
\]

**Interprétation** : \(PV = 0.9362 > 0.05\), donc on accepte \(H_0\) pour tout seuil \(\alpha < 0.9362\).

#### 4. Test d'ajustement du khi-deux

**Étape 1** : Hypothèses

\[
H_0 : X \sim N(10, 0.25) \quad \text{vs} \quad H_1 : X \not\sim N(10, 0.25)
\]

**Étape 2** : Calculer les effectifs attendus

Pour chaque intervalle, on calcule \(p_i^{(0)} = P(X \in \text{intervalle} | H_0)\) avec \(X \sim N(10, 0.5^2)\).

- **Intervalle [9.5, 9.75[** :
  \[
  p_1 = P(9.5 \leq X < 9.75) = \Phi\left(\frac{9.75-10}{0.5}\right) - \Phi\left(\frac{9.5-10}{0.5}\right)
  \]
  \[
  = \Phi(-0.5) - \Phi(-1) = (1 - 0.6915) - (1 - 0.8413) = 0.1498
  \]
  \[
  E_1 = 25 \times 0.1498 = 3.745
  \]

- **Intervalle [9.75, 10[** :
  \[
  p_2 = P(9.75 \leq X < 10) = \Phi(0) - \Phi(-0.5) = 0.5 - 0.3085 = 0.1915
  \]
  \[
  E_2 = 25 \times 0.1915 = 4.788
  \]

- **Intervalle [10, 10.25[** :
  \[
  p_3 = P(10 \leq X < 10.25) = \Phi(0.5) - \Phi(0) = 0.6915 - 0.5 = 0.1915
  \]
  \[
  E_3 = 25 \times 0.1915 = 4.788
  \]

- **Intervalle [10.25, 10.5[** :
  \[
  p_4 = P(10.25 \leq X < 10.5) = \Phi(1) - \Phi(0.5) = 0.8413 - 0.6915 = 0.1498
  \]
  \[
  E_4 = 25 \times 0.1498 = 3.745
  \]

**Vérification** : \(E_1 + E_2 + E_3 + E_4 = 3.745 + 4.788 + 4.788 + 3.745 = 17.066\)

Il manque les probabilités pour \(X < 9.5\) et \(X \geq 10.5\). On doit ajuster ou regrouper.

**Ajustement** : On regroupe les classes extrêmes.

| Intervalle | Effectifs observés (\(O_i\)) | Effectifs attendus (\(E_i\)) | \(\frac{(O_i - E_i)^2}{E_i}\) |
|------------|----------------------------|----------------------------|------------------------------|
| [9.5, 9.75[ | 3 | 3.745 | 0.149 |
| [9.75, 10[ | 8 | 4.788 | 2.158 |
| [10, 10.25[ | 10 | 4.788 | 5.678 |
| [10.25, 10.5[ | 4 | 3.745 | 0.017 |
| **Total** | **25** | **17.066** | **8.002** |

**Problème** : Les effectifs attendus ne somment pas à 25. Il faut recalculer en incluant toutes les probabilités ou en normalisant.

**Recalcul correct** : On inclut \(P(X < 9.5)\) et \(P(X \geq 10.5)\) dans les classes extrêmes.

\[
P(X < 9.5) = \Phi(-1) = 0.1587, \quad P(X \geq 10.5) = 1 - \Phi(1) = 0.1587
\]

En regroupant :
- Classe 1 : \(X < 9.75\) → \(E_1 = 25 \times (0.1587 + 0.1498) = 7.7125\)
- Classe 2 : \(9.75 \leq X < 10\) → \(E_2 = 4.788\)
- Classe 3 : \(10 \leq X < 10.25\) → \(E_3 = 4.788\)
- Classe 4 : \(X \geq 10.25\) → \(E_4 = 25 \times (0.1498 + 0.1587) = 7.7125\)

**Étape 3** : Calculer \(\chi_0^2\)

\[
\chi_0^2 = \sum_{i=1}^{4} \frac{(O_i - E_i)^2}{E_i}
\]

\[
= \frac{(3 - 7.7125)^2}{7.7125} + \frac{(8 - 4.788)^2}{4.788} + \frac{(10 - 4.788)^2}{4.788} + \frac{(4 - 7.7125)^2}{7.7125}
\]

\[
= \frac{22.19}{7.7125} + \frac{10.32}{4.788} + \frac{27.17}{4.788} + \frac{13.79}{7.7125}
\]

\[
= 2.88 + 2.15 + 5.68 + 1.79 = 12.50
\]

**Étape 4** : Degrés de liberté

\[
\nu = k - p - 1 = 4 - 0 - 1 = 3
\]

(Aucun paramètre estimé car \(\mu = 10\) et \(\sigma = 0.5\) sont connus)

**Étape 5** : Règle de décision

Pour \(\alpha = 0.05\) et \(\nu = 3\), on a \(\chi_{0.05; 3}^2 \approx 7.815\).

\[
\chi_0^2 = 12.50 > 7.815
\]

**Conclusion** : On **rejette \(H_0\)** au seuil 5%. Les diamètres ne suivent pas une loi normale \(N(10, 0.25)\).

---

## 11. VALEURS CRITIQUES USUELLES

### Loi normale standard

| \(\alpha\) | \(z_{\alpha}\) | \(z_{\alpha/2}\) |
|-----------|----------------|-----------------|
| 0.10 | 1.282 | 1.645 |
| 0.05 | 1.645 | 1.960 |
| 0.01 | 2.326 | 2.576 |

### Loi de Student (exemples)

| ddl | \(t_{0.05}\) | \(t_{0.025}\) |
|-----|-------------|---------------|
| 10 | 1.812 | 2.228 |
| 20 | 1.725 | 2.086 |
| 30 | 1.697 | 2.042 |
| \(\infty\) | 1.645 | 1.960 |

### Loi du khi-deux (exemples)

| ddl | \(\chi_{0.05}^2\) | \(\chi_{0.01}^2\) |
|-----|------------------|------------------|
| 1 | 3.841 | 6.635 |
| 2 | 5.991 | 9.210 |
| 3 | 7.815 | 11.345 |
| 5 | 11.070 | 15.086 |
| 10 | 18.307 | 23.209 |

