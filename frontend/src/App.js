import React, { useState } from 'react';
import { AlertTriangle, X, Link2 } from 'lucide-react';
import './index.css';

const classifyProductApi = async (productUrl) => {
    const response = await fetch('/api/classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: productUrl }),
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || `An unexpected API error occurred. Status: ${response.status}`);
    }
    
    return data;
};

const ErrorDisplay = ({ error, clearError }) => {
    if (!error) return null;
    return (
        <div className="mt-6 p-4 bg-red-900/50 border border-red-700 text-red-300 rounded-lg flex justify-between items-center animate-fade-in">
            <div className="flex items-center">
                <AlertTriangle className="w-5 h-5 mr-3 flex-shrink-0" />
                <p className="text-sm">{error}</p>
            </div>
            <button onClick={clearError} className="p-1 rounded-full hover:bg-red-800/50 transition-colors">
                <X className="w-4 h-4" />
            </button>
        </div>
    );
};

const AttributeTable = ({ title, data }) => (
    <div className="mb-8">
        <h3 className="text-lg font-semibold text-slate-200 border-b border-slate-700 pb-2 mb-4">{title}</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-6 gap-y-4">
            {Object.entries(data).map(([key, value]) => (
                <div key={key} className="flex flex-col">
                    <span className="text-xs text-slate-400">{key}</span>
                    <span className="text-sm font-medium text-slate-100">{String(value)}</span>
                </div>
            ))}
        </div>
    </div>
);

const ResultsDisplay = ({ results }) => {
    if (!results) return null;

    const { productTitle, classifiedAttributes } = results;

    return (
        <div className="mt-8 p-6 md:p-8 bg-slate-800/50 border border-slate-700 rounded-xl transition-height overflow-hidden animate-fade-in">
            <h2 className="text-xl font-bold text-white mb-6">{productTitle}</h2>
            <AttributeTable title="Global Attributes" data={classifiedAttributes.global} />
            <AttributeTable title="Category-Specific Attributes" data={classifiedAttributes.categorySpecific} />
        </div>
    );
};

function App() {
    const [url, setUrl] = useState('https://www.noon.com/uae-en/june-women-viscose-patterned-wide-fit-maxi-dress-green-navy/N53401564A/p/');
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [results, setResults] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setError(null);
        setResults(null);

        try {
            const responseData = await classifyProductApi(url);
            setResults(responseData);
        } catch (err) {
            setError(err.message || "An unknown error occurred.");
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-slate-900 text-slate-300 font-sans antialiased p-4 sm:p-6 lg:p-8">
            <div className="w-full max-w-3xl mx-auto">
                <header className="text-center mb-8">
                    <h1 className="text-4xl sm:text-5xl font-bold text-white tracking-tight">AI Product Classifier</h1>
                    <p className="mt-3 text-lg text-slate-400 max-w-2xl mx-auto">Enter a Noon.com product URL to dynamically identify its attributes using AI.</p>
                </header>

                <main>
                    <div className="glass-card rounded-xl shadow-2xl shadow-slate-950/50 p-6 md:p-8">
                        <form onSubmit={handleSubmit}>
                            <label htmlFor="url-input" className="block text-sm font-medium text-slate-300 mb-2">
                                Product URL
                            </label>
                            <div className="relative flex items-center">
                                <Link2 className="absolute left-3 w-5 h-5 text-slate-500 pointer-events-none" />
                                <input
                                    type="url"
                                    id="url-input"
                                    value={url}
                                    onChange={(e) => setUrl(e.target.value)}
                                    placeholder="e.g., https://www.noon.com/..."
                                    className="w-full bg-slate-800/70 border border-slate-700 text-slate-200 rounded-md pl-10 pr-32 py-2.5 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
                                    required
                                    disabled={isLoading}
                                />
                                <button 
                                    type="submit" 
                                    disabled={isLoading}
                                    className="absolute right-1.5 top-1/2 -translate-y-1/2 flex items-center justify-center h-9 px-4 text-sm font-semibold rounded-md transition-all duration-200 ease-in-out bg-indigo-600 text-white hover:bg-indigo-500 disabled:bg-slate-600 disabled:text-slate-400 disabled:cursor-not-allowed"
                                >
                                    {isLoading ? <span className="spinner !w-5 !h-5 !border-2"></span> : "Classify"}
                                </button>
                            </div>
                        </form>
                    </div>

                    <ErrorDisplay error={error} clearError={() => setError(null)} />
                    <ResultsDisplay results={results} />
                </main>
                
                <footer className="text-center mt-12">
                    <p className="text-sm text-slate-500">Designed & Engineered by Neo</p>
                </footer>
            </div>
        </div>
    );
}

export default App;
