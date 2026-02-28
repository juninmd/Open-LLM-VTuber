```markdown
# AGENTS.md - Guidelines for AI Coding Agents

These guidelines are designed to ensure high-quality, maintainable, and robust AI coding agents. Adherence to these principles is mandatory for all development activities.

## 1. DRY (Don't Repeat Yourself)

*   **Single Responsibility Principle:** Each agent should have a single, clearly defined purpose.
*   **Abstraction:** Utilize abstract classes and interfaces to decouple components and promote reusability.
*   **Module Structure:** Organize code into logical modules with well-defined responsibilities.
*   **Code Reuse:** Create reusable components and functions whenever possible. Avoid duplicating logic.

## 2. KISS (Keep It Simple, Stupid)

*   **Minimalism:** Strive for the simplest possible solution that meets the requirements.
*   **Readability:** Write code that is easy to understand, even for non-expert developers.
*   **Clear Naming:** Use descriptive and consistent names for variables, functions, and classes.
*   **Concise Logic:** Keep functions and code as short as possible without sacrificing clarity.

## 3. SOLID Principles

*   **Single Responsibility:** Each class should have only one reason to change.
*   **Open/Closed Principle:** Classes should be open for extension but closed for modification.
*   **Liskov Substitution Principle:** Subclasses should be able to replace the base class without affecting the correctness of the program.
*   **Interface Segregation Principle:** Client code should not need to establish dependencies with other code that it does not use.
*   **Dependency Inversion Principle:** High-level modules should not depend on low-level modules.

## 4. YAGNI (You Aren't Gonna Need It)

*   **Avoid Unnecessary Complexity:** Implement only the features necessary for the current task.
*   **Progressive Complexity:** Build upon existing functionality rather than trying to solve everything at once.
*   **Refactoring:** Refactor code to improve its structure and design without altering its behavior.

## 5. Development Process & Code Quality

*   **Line Length:** Each file should be limited to 180 lines of code.
*   **Comments:**  Add concise, informative comments where needed to explain complex logic or non-obvious decisions.  Prioritize clarity over extensive documentation.
*   **Testing:** All development must be productive.  Use mocks only for unit testing.  No real implementation is permitted.
*   **Code Review:** Every proposed change or modification should undergo a thorough code review process.
*   **Version Control:** Utilize Git for version control and adhere to established branching strategies.

## 6.  File Structure & Content (Example - Adjust as needed)

*   **`src/agent/`**: Core agent logic.
*   **`src/core/`**:  Reusable components and utilities.
*   **`src/data/`**: Data handling and persistence.
*   **`src/communication/`**:  Communication protocols and agent interaction.
*   **`src/analytics/`**:  Logging, monitoring, and data analysis.
*   **`src/config/`**: Configuration settings.
*   **`src/tests/`**: Unit and integration tests.
*   **`src/README.md`**:  Project overview, setup instructions, and contribution guidelines.

## 7.  Specific Requirements (Example – Adapt to Agent's Functionality)

*   **State Management:** Implement a robust state management system (e.g., a simple dictionary or a dedicated state management library).
*   **Event Handling:** Provide a clear and consistent system for handling events and triggers.
*   **Agent Communication:** Define a standardized communication protocol for agents to exchange data.
*   **Error Handling:** Implement comprehensive error handling with logging.

## 8.  Tools & Technologies

*   **Language:**  Specify the primary programming language (e.g., Python, JavaScript).
*   **Libraries:** List key libraries/frameworks to be used.
*   **Testing Framework:** Specify a testing framework (e.g., pytest, Jest).

## 9.  Documentation

*   **API Documentation:**  Provide clear documentation for all APIs and functions.
*   **Code Comments:**  Thoroughly comment the code to explain its functionality.

## 10.  Continuous Improvement

*   **Regular Reviews:** Conduct regular code reviews to identify potential issues and ensure adherence to guidelines.
*   **Refactoring:** Continuously refactor code to improve its structure and maintainability.

These guidelines are intended as a foundational framework.  Adapt and refine them as the AGENTS.md repository evolves.  All contributions should align with these principles.
```