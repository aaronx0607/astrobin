/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.5
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

namespace Xapian {

using System;
using System.Runtime.InteropServices;

public class PositionIterator : IDisposable {
  private HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal PositionIterator(IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new HandleRef(this, cPtr);
  }

  internal static HandleRef getCPtr(PositionIterator obj) {
    return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
  }

  ~PositionIterator() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          XapianPINVOKE.delete_PositionIterator(swigCPtr);
        }
        swigCPtr = new HandleRef(null, IntPtr.Zero);
      }
      GC.SuppressFinalize(this);
    }
  }

    public static PositionIterator operator++(PositionIterator it) {
	return it.Next();
    }
    public override bool Equals(object o) {
	return o is PositionIterator && Equals((PositionIterator)o);
    }
    public static bool operator==(PositionIterator a, PositionIterator b) {
	if ((object)a == (object)b) return true;
	if ((object)a == null || (object)b == null) return false;
	return a.Equals(b);
    }
    public static bool operator!=(PositionIterator a, PositionIterator b) {
	if ((object)a == (object)b) return false;
	if ((object)a == null || (object)b == null) return true;
	return !a.Equals(b);
    }
    // Implementing GetHashCode() to always return 0 is rather lame, but
    // using iterators as keys in a hash table would be rather strange.
    public override int GetHashCode() { return 0; }

  public PositionIterator() : this(XapianPINVOKE.new_PositionIterator__SWIG_0(), true) {
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
  }

  public PositionIterator(PositionIterator other) : this(XapianPINVOKE.new_PositionIterator__SWIG_1(PositionIterator.getCPtr(other)), true) {
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
  }

  public uint GetTermPos() {
    uint ret = XapianPINVOKE.PositionIterator_GetTermPos(swigCPtr);
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
    return ret;
  }

  public PositionIterator Next() {
    PositionIterator ret = new PositionIterator(XapianPINVOKE.PositionIterator_Next(swigCPtr), false);
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
    return ret;
  }

  public bool Equals(PositionIterator other) {
    bool ret = XapianPINVOKE.PositionIterator_Equals(swigCPtr, PositionIterator.getCPtr(other));
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
    return ret;
  }

  public void SkipTo(uint pos) {
    XapianPINVOKE.PositionIterator_SkipTo(swigCPtr, pos);
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
  }

  public string GetDescription() {
    string ret = XapianPINVOKE.PositionIterator_GetDescription(swigCPtr);
    if (XapianPINVOKE.SWIGPendingException.Pending) throw XapianPINVOKE.SWIGPendingException.Retrieve();
    return ret;
  }

}

}
