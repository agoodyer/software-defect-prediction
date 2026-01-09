# 🔍 Software Defect Prediction

**An Exploration of Model Interpretability in Software Defect Analysis**

This project investigates whether static code metrics (e.g., Lines of Code, Cyclomatic Complexity) are actually legitimate predictors of software defects. Driven by **Goodhart’s Law**—*"When a measure becomes a target, it ceases to be a good measure"*—we focus on feature selection and model interpretability over raw predictive accuracy.

---

## 🛠️ Methodology

The core implementation utilizes a **Logistic Regression model** trained via gradient descent, specifically modified for the defect prediction domain:

*  **L1 Regularization (Lasso):** Encourages sparsity in learned weights to drive irrelevant metrics to zero, effectively surfacing only the most "useful" predictors.


*  **Asymmetric Loss Function:** To address the severe consequences of missing a real defect, the model applies a **4x heavier penalty** for misclassifying a true defect (False Negative) compared to a false alarm (False Positive).


*  **Feature Scaling:** Inputs undergo log-transformation to compress power-law distributions, followed by Z-score normalization to ensure fair comparison of feature importance.


*  **FCNN Baseline:** A two-layer Fully Connected Neural Network (ReLU activation, 50% Dropout) serves as a performance benchmark.



---

## 📊 Evaluation & Results

### Feature Importance (NASA PROMISE)

The L1-regularized model successfully isolated **6 critical metrics** from the original 21, zeroing out those with low relative importance.

| Rank | Metric | Weight | Impact | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Unique Operands** | 0.2456 | $\uparrow$ | Large "vocabularies" increase state complexity, making logic errors more likely. |
| 2 | **Executable LOC** | 0.1657 | $\uparrow$ | Larger programs naturally provide more opportunities for defects to exist. |
| 3 | **Lines of Comments** | 0.0970 | $\uparrow$ | Often a proxy for "difficult" code where non-trivial logic requires heavy documentation. |
| 4 | **Design Complexity** | 0.0709 | $\uparrow$ | Focuses on modules with many external calls; "high traffic" modules are more bug-prone. |
| 5 | **Cyclomatic Complexity** | 0.0679 | $\uparrow$ | High path counts are difficult to test exhaustively, leading to uncovered edge cases. |
| 6 | **Halstead Error Est** | 0.0393 | $\uparrow$ | An aggregate measure specifically engineered to estimate software defects. |

### Performance Metrics

The model was evaluated using an 80/20 stratified split to account for significant class imbalance (most modules are defect-free).

*  **Logistic Regression Accuracy:** ~71.68%.


*  **FCNN Accuracy:** ~75.64%.



---

## 🚀 Key Conclusions

*  **The Information Gap:** Models relying solely on static metrics possess a fundamental bias; semantic errors (e.g., a loop starting at index 1 instead of 0) are invisible to these features, creating a natural upper bound on accuracy.


*  **Engineering Best Practices:** The high impact of module size (LOC) and complexity validates design patterns that promote **small, modular, and single-responsibility** artifacts.


*  **Strategic Focus:** Instead of exhaustively satisfying all static code checks, engineers should prioritize high-impact metrics monitoring **complexity, state, and coupling**.



---

## 👥 Authors

*  **Aidan Goodyer** – Software Engineering, McMaster University 


*  **Mason Azzopardi**– Software Engineering, McMaster University 
