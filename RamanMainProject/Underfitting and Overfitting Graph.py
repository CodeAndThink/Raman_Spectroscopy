import matplotlib.pyplot as plt

# Đây chỉ là một ví dụ giả định về dữ liệu loss và validation loss
epochs = [1, 2, 3, 4, 5]
training_loss = [0.8, 0.75, 0.72, 0.7, 0.68]
validation_loss = [1.2, 1.15, 1.1, 1.08, 1.06]

plt.plot(epochs, training_loss, label='Training Loss')
plt.plot(epochs, validation_loss, label='Validation Loss')
plt.title('Underfitting Model - Loss and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Đây chỉ là một ví dụ giả định về dữ liệu loss và validation loss
epochs = [1, 2, 3, 4, 5]
training_loss = [0.8, 0.6, 0.4, 0.2, 0.1]  # Giảm dần
validation_loss = [1.0, 1.2, 1.5, 2.0, 2.5]  # Tăng lên sau một số epoch

plt.plot(epochs, training_loss, label='Training Loss')
plt.plot(epochs, validation_loss, label='Validation Loss')
plt.title('Overfitting Model - Loss and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

import matplotlib.pyplot as plt

# Đây chỉ là một ví dụ giả định về dữ liệu loss và validation loss
epochs = [1, 2, 3, 4, 5]
training_loss = [0.8, 0.6, 0.4, 0.3, 0.2]  # Giảm dần và ổn định
validation_loss = [0.9, 0.7, 0.5, 0.4, 0.3]  # Giảm dần và ổn định

plt.plot(epochs, training_loss, label='Training Loss')
plt.plot(epochs, validation_loss, label='Validation Loss')
plt.title('Well-fitted Model - Loss and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

