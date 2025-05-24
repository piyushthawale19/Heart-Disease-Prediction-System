/**
 * Smart Heart Disease Prediction System
 * Frontend JavaScript functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initializeFormValidation();
    initializeProgressTracking();
    initializeSliders();
    initializeTooltips();
    initializeAnimations();
});

/**
 * Form Validation
 */
function initializeFormValidation() {
    const form = document.getElementById('healthForm');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        if (!validateForm()) {
            e.preventDefault();
            showAlert('Please fill in at least one health parameter before submitting.', 'warning');
        }
    });
}

function validateForm() {
    const form = document.getElementById('healthForm');
    const inputs = form.querySelectorAll('input, select');
    let hasValue = false;

    inputs.forEach(input => {
        if (input.value && input.value.trim() !== '') {
            hasValue = true;
        }
    });

    return hasValue;
}

/**
 * Progress Tracking
 */
function initializeProgressTracking() {
    const form = document.getElementById('healthForm');
    if (!form) return;

    const inputs = form.querySelectorAll('input, select');
    
    inputs.forEach(input => {
        input.addEventListener('change', updateProgress);
        input.addEventListener('input', updateProgress);
    });

    // Initial progress calculation
    updateProgress();
}

function updateProgress() {
    const form = document.getElementById('healthForm');
    const progressBar = document.getElementById('form-progress');
    
    if (!form || !progressBar) return;

    const inputs = form.querySelectorAll('input, select');
    let filled = 0;
    let total = inputs.length;

    inputs.forEach(input => {
        if (input.value && input.value.trim() !== '') {
            filled++;
        }
    });

    const percentage = Math.round((filled / total) * 100);
    progressBar.style.width = percentage + '%';
    progressBar.setAttribute('aria-valuenow', percentage);

    // Update progress bar color based on completion
    progressBar.className = 'progress-bar';
    if (percentage < 25) {
        progressBar.classList.add('bg-danger');
    } else if (percentage < 50) {
        progressBar.classList.add('bg-warning');
    } else if (percentage < 75) {
        progressBar.classList.add('bg-info');
    } else {
        progressBar.classList.add('bg-success');
    }
}

/**
 * Range Slider Handling
 */
function initializeSliders() {
    // Physical Activity Slider
    const activitySlider = document.getElementById('physical_activity');
    const activityValue = document.getElementById('activity-value');
    
    if (activitySlider && activityValue) {
        activitySlider.addEventListener('input', function() {
            activityValue.textContent = this.value;
            updateSliderBadgeColor(activityValue, this.value, 10);
        });
        
        // Initialize value
        activityValue.textContent = activitySlider.value;
        updateSliderBadgeColor(activityValue, activitySlider.value, 10);
    }

    // Stress Level Slider
    const stressSlider = document.getElementById('stress_level');
    const stressValue = document.getElementById('stress-value');
    
    if (stressSlider && stressValue) {
        stressSlider.addEventListener('input', function() {
            stressValue.textContent = this.value;
            updateSliderBadgeColor(stressValue, this.value, 10, true);
        });
        
        // Initialize value
        stressValue.textContent = stressSlider.value;
        updateSliderBadgeColor(stressValue, stressSlider.value, 10, true);
    }
}

function updateSliderBadgeColor(badge, value, max, isReverse = false) {
    badge.className = 'badge';
    
    const percentage = (value / max) * 100;
    
    if (isReverse) {
        // For stress level - higher is worse
        if (percentage <= 33) {
            badge.classList.add('bg-success');
        } else if (percentage <= 66) {
            badge.classList.add('bg-warning');
        } else {
            badge.classList.add('bg-danger');
        }
    } else {
        // For activity level - higher is better
        if (percentage <= 33) {
            badge.classList.add('bg-danger');
        } else if (percentage <= 66) {
            badge.classList.add('bg-warning');
        } else {
            badge.classList.add('bg-success');
        }
    }
}

/**
 * Tooltips and Help Text
 */
function initializeTooltips() {
    // Add tooltips to form fields with medical terminology
    const tooltipData = {
        'cp': 'Type of chest pain experienced: Typical angina, atypical angina, non-anginal pain, or asymptomatic',
        'trestbps': 'Blood pressure measured when the heart is at rest between beats',
        'chol': 'Total cholesterol level in the blood',
        'fbs': 'Whether fasting blood sugar level is greater than 120 mg/dl',
        'restecg': 'Results of electrocardiogram taken while at rest',
        'thalach': 'Maximum heart rate achieved during exercise stress test',
        'exang': 'Whether exercise induces chest pain (angina)',
        'oldpeak': 'ST depression induced by exercise relative to rest',
        'slope': 'Slope of the peak exercise ST segment',
        'ca': 'Number of major vessels colored by fluoroscopy',
        'thal': 'Thalassemia - a blood disorder affecting hemoglobin'
    };

    Object.keys(tooltipData).forEach(fieldId => {
        const field = document.getElementById(fieldId);
        if (field) {
            field.setAttribute('title', tooltipData[fieldId]);
            field.setAttribute('data-bs-toggle', 'tooltip');
        }
    });

    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Animations and Visual Effects
 */
function initializeAnimations() {
    // Fade in cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe all cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        observer.observe(card);
    });

    // Animate statistics on landing page
    animateStats();
}

function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-number');
    
    statNumbers.forEach(stat => {
        const target = parseInt(stat.textContent.replace(/[^\d]/g, ''));
        if (target) {
            animateNumber(stat, target);
        }
    });
}

function animateNumber(element, target) {
    let current = 0;
    const increment = target / 50;
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        
        // Format the number
        if (target >= 1000) {
            element.textContent = Math.floor(current).toLocaleString() + '+';
        } else if (element.textContent.includes('%')) {
            element.textContent = Math.floor(current) + '%';
        } else {
            element.textContent = Math.floor(current);
        }
    }, 20);
}

/**
 * Alert System
 */
function showAlert(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show`;
    alertContainer.setAttribute('role', 'alert');
    
    alertContainer.innerHTML = `
        <i class="fas fa-${getAlertIcon(type)} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

    // Insert at the top of the main content
    const main = document.querySelector('main');
    if (main) {
        main.insertBefore(alertContainer, main.firstChild);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (alertContainer.parentNode) {
                alertContainer.remove();
            }
        }, 5000);
    }
}

function getAlertIcon(type) {
    const icons = {
        'success': 'check-circle',
        'warning': 'exclamation-triangle',
        'danger': 'exclamation-circle',
        'info': 'info-circle'
    };
    return icons[type] || 'info-circle';
}

/**
 * Form Auto-save (Optional Enhancement)
 */
function initializeAutoSave() {
    const form = document.getElementById('healthForm');
    if (!form) return;

    const inputs = form.querySelectorAll('input, select');
    
    inputs.forEach(input => {
        // Load saved value
        const saved = localStorage.getItem(`health_form_${input.name}`);
        if (saved && !input.value) {
            input.value = saved;
        }

        // Save on change
        input.addEventListener('change', function() {
            if (this.value) {
                localStorage.setItem(`health_form_${this.name}`, this.value);
            } else {
                localStorage.removeItem(`health_form_${this.name}`);
            }
        });
    });
}

/**
 * Clear Form Data
 */
function clearFormData() {
    const form = document.getElementById('healthForm');
    if (!form) return;

    // Clear form
    form.reset();
    
    // Clear localStorage
    const inputs = form.querySelectorAll('input, select');
    inputs.forEach(input => {
        localStorage.removeItem(`health_form_${input.name}`);
    });
    
    // Reset progress
    updateProgress();
    
    showAlert('Form data cleared successfully.', 'success');
}

/**
 * Print Results Function
 */
function printResults() {
    window.print();
}

/**
 * Export Results (Optional Enhancement)
 */
function exportResults() {
    const results = document.querySelector('.results-main');
    if (!results) return;

    // Create a simplified version for export
    const exportContent = results.cloneNode(true);
    
    // Remove interactive elements
    const buttons = exportContent.querySelectorAll('button, .btn');
    buttons.forEach(btn => btn.remove());

    // Create export window
    const exportWindow = window.open('', '_blank');
    exportWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Heart Health Assessment Results</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { font-family: Arial, sans-serif; }
                .card { margin-bottom: 1rem; }
                @media print { body { margin: 0; } }
            </style>
        </head>
        <body>
            ${exportContent.innerHTML}
        </body>
        </html>
    `);
    exportWindow.document.close();
}

/**
 * Utility Functions
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Make some functions globally available
window.clearFormData = clearFormData;
window.printResults = printResults;
window.exportResults = exportResults;
