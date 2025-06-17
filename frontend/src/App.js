import React, { useState } from 'react';
import './App.css';

function App() {
  const [activeSection, setActiveSection] = useState('home');

  const products = [
    {
      id: 'temp-spoofer',
      name: 'Temp Spoofer',
      description: 'Resets on restart - Budget-friendly option for temporary identity masking',
      weeklyPrice: 5,
      monthlyPrice: 15,
      features: ['Temporary protection', 'Easy to use', 'Budget-friendly', 'Quick setup']
    },
    {
      id: 'perm-spoofer',
      name: 'Perm Spoofer',
      description: 'Survives reboot and supports automatic updates for continuous protection',
      weeklyPrice: 15,
      monthlyPrice: 40,
      features: ['Permanent protection', 'Survives restarts', 'Auto-updates', 'Advanced features']
    },
    {
      id: 'fortnite-cheat',
      name: 'Fortnite Public Cheat',
      description: 'Complete Fortnite enhancement suite with aimbot, ESP, anti-ban protection',
      weeklyPrice: 10,
      monthlyPrice: 30,
      features: ['Aimbot system', 'ESP/Wallhacks', 'Anti-ban protection', 'Regular updates']
    }
  ];

  const ContactModal = ({ isOpen, onClose, productName }) => {
    if (!isOpen) return null;

    return (
      <div className="modal-overlay" onClick={onClose}>
        <div className="modal-content" onClick={e => e.stopPropagation()}>
          <button className="modal-close" onClick={onClose}>×</button>
          <h3>Purchase {productName}</h3>
          <div className="contact-info">
            <p className="contact-method">
              <span className="contact-label">📧 Email:</span>
              <span className="contact-value">doddggy@mail.io</span>
            </p>
            <p className="contact-method">
              <span className="contact-label">💬 Discord:</span>
              <a href="https://discord.gg/x2n3b6teqw" target="_blank" rel="noopener noreferrer" className="discord-link">
                Join Server
              </a>
            </p>
            <p className="contact-note">
              Contact us through either method to complete your purchase!
            </p>
          </div>
        </div>
      </div>
    );
  };

  const [modalOpen, setModalOpen] = useState(false);
  const [selectedProduct, setSelectedProduct] = useState('');

  const openModal = (productName) => {
    setSelectedProduct(productName);
    setModalOpen(true);
  };

  return (
    <div className="App">
      {/* Navigation */}
      <nav className="navbar">
        <div className="nav-container">
          <div className="nav-brand">
            <span className="brand-text">FLUXWARE</span>
          </div>
          <div className="nav-menu">
            <button 
              className={`nav-item ${activeSection === 'home' ? 'active' : ''}`}
              onClick={() => setActiveSection('home')}
            >
              Home
            </button>
            <button 
              className={`nav-item ${activeSection === 'shop' ? 'active' : ''}`}
              onClick={() => setActiveSection('shop')}
            >
              Shop
            </button>
            <button 
              className={`nav-item ${activeSection === 'about' ? 'active' : ''}`}
              onClick={() => setActiveSection('about')}
            >
              About
            </button>
          </div>
        </div>
      </nav>

      {/* Home Section */}
      {activeSection === 'home' && (
        <div className="hero-section">
          <div className="hero-content">
            <h1 className="hero-title">
              <span className="flux">FLUX</span><span className="ware">WARE</span>
            </h1>
            <p className="hero-subtitle">Premium Gaming Tools & Enhancements</p>
            <p className="hero-description">
              Elevate your gaming experience with our cutting-edge spoofers and cheats. 
              Join the elite gaming community.
            </p>
            <button 
              className="cta-button"
              onClick={() => setActiveSection('shop')}
            >
              Explore Products
            </button>
          </div>
          <div className="stats-grid">
            <div className="stat-item">
              <span className="stat-number">1000+</span>
              <span className="stat-label">Active Users</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">99.9%</span>
              <span className="stat-label">Uptime</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">24/7</span>
              <span className="stat-label">Support</span>
            </div>
          </div>
        </div>
      )}

      {/* Shop Section */}
      {activeSection === 'shop' && (
        <div className="shop-section">
          <div className="section-header">
            <h2 className="section-title">Premium Products</h2>
            <p className="section-subtitle">Choose your gaming enhancement</p>
          </div>
          
          <div className="products-grid">
            {products.map((product) => (
              <div key={product.id} className="product-card">
                <div className="product-header">
                  <h3 className="product-name">{product.name}</h3>
                  <p className="product-description">{product.description}</p>
                </div>
                
                <div className="product-features">
                  {product.features.map((feature, index) => (
                    <div key={index} className="feature-item">
                      <span className="feature-check">✓</span>
                      <span className="feature-text">{feature}</span>
                    </div>
                  ))}
                </div>
                
                <div className="pricing-section">
                  <div className="price-option">
                    <span className="price-duration">Weekly</span>
                    <span className="price-amount">${product.weeklyPrice}</span>
                    <button 
                      className="purchase-btn weekly"
                      onClick={() => openModal(product.name + ' (Weekly)')}
                    >
                      Purchase Weekly
                    </button>
                  </div>
                  
                  <div className="price-option featured">
                    <span className="price-badge">BEST VALUE</span>
                    <span className="price-duration">Monthly</span>
                    <span className="price-amount">${product.monthlyPrice}</span>
                    <button 
                      className="purchase-btn monthly"
                      onClick={() => openModal(product.name + ' (Monthly)')}
                    >
                      Purchase Monthly
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* About Section */}
      {activeSection === 'about' && (
        <div className="about-section">
          <div className="about-content">
            <h2 className="section-title">About FluxWare</h2>
            <div className="about-grid">
              <div className="about-card">
                <div className="about-icon">🚀</div>
                <h3>Premium Quality</h3>
                <p>Our tools are developed with the highest quality standards, ensuring reliable performance and safety.</p>
              </div>
              <div className="about-card">
                <div className="about-icon">🛡️</div>
                <h3>Secure & Safe</h3>
                <p>Advanced anti-detection technology keeps you protected while using our enhancement tools.</p>
              </div>
              <div className="about-card">
                <div className="about-icon">👥</div>
                <h3>Community Driven</h3>
                <p>Join our Discord community for support, updates, and connecting with fellow gamers.</p>
              </div>
              <div className="about-card">
                <div className="about-icon">⚡</div>
                <h3>Regular Updates</h3>
                <p>Continuous updates and improvements to stay ahead of game patches and security measures.</p>
              </div>
            </div>
            
            <div className="discord-section">
              <h3>Join Our Community</h3>
              <p>Connect with other users, get support, and stay updated with the latest features.</p>
              <a href="https://discord.gg/x2n3b6teqw" target="_blank" rel="noopener noreferrer" className="discord-button">
                Join Discord Server
              </a>
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <p>&copy; 2025 FluxWare. Premium Gaming Tools.</p>
          <p>Contact: doddggy@mail.io</p>
        </div>
      </footer>

      {/* Contact Modal */}
      <ContactModal 
        isOpen={modalOpen} 
        onClose={() => setModalOpen(false)}
        productName={selectedProduct}
      />
    </div>
  );
}

export default App;