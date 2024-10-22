'use client';
import Link from 'next/link';
import { useState } from 'react';

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <header className="bg-white border-b-2 text-[#000] py-4 px-6 flex items-center justify-between shadow-md">
      <Link href="/" legacyBehavior>
        <a className="flex items-center">
          <img src="/logo.png" alt="mockInterview Logo" className="w-8 h-8 mr-4" />
          <span className="text-xl"><span className='font-bold'>Mock</span> Interview</span>
        </a>
      </Link>

      <nav className={`space-x-6 flex`}>
        <div className={`hidden md:flex gap-5`}>
        <Link href="/learn" className={`hidden md:block`} legacyBehavior>
          <a className="hover:text-gray-600 pt-1">Learn More</a>
        </Link>
        <Link href="/list-course" className={`hidden md:block`} legacyBehavior>
          <a className="hover:text-gray-600 border-[3px] p-1 border-[#BA932F] font-bold">Explore Course List</a>
        </Link>
        </div>
        <Link href="/login" legacyBehavior>
          <a className="hover:text-gray-600 text-black p-1 px-2 bg-[#BA932F] font-bold">Login/Signup</a>
        </Link>
      </nav>

      {/* <button
        className={`md:hidden ${isOpen ? 'hidden' : ''}`}
        onClick={toggleMenu}
      >
        <svg
          className="w-6 h-6"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fillRule="evenodd"
            d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z"
            clipRule="evenodd"
          />
        </svg>
      </button> */}
    </header>
  );
}

export default Navbar;
